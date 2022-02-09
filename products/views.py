from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator 
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand, ProductReview
from profiles.models import UserProfile
from .forms import ProductForm, ReviewForm

# Create your views here.

def all_products(request):
    """ A view to show all CSC products """

    products = Product.objects.all()
    selected_category = None
    selected_brand = None
    query = None
    categories = None
    sort = None
    direction = None
    brands = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            print(request.GET['category'])
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            selected_category = request.GET['category']

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)
            selected_brand = request.GET['brand']

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    
    # pagination but broke filtering
    # pagination = Paginator(Product.objects.all(), 12)
    # page = request.GET.get('page')
    # product_list = pagination.get_page(page)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_brands': brands,
        'current_sorting': current_sorting,
        'active_category': selected_category,
        'active_brand': selected_brand,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

# Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        review_text = request.POST.get('review_text', '')
        recommended = request.POST.get('recommended', True)
        reviews = product.reviews.all()

        # if reviews.filter(user=request.user).exists():
        #     messages.error(
        #         request, "You've already reviewed this product")
        #     return redirect(reverse('product_detail', args=[product.id]))
        # else:
        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, review_text=review_text, recommended=recommended)

        messages.success(
            request,
            "You have succesfully added a product review!")

        return redirect(reverse('product_detail', args=[product.id]))

    context = {
         'product': product,
        #  'review': review,
        #  'reviews': reviews,
    }

    return render(request, 'products/product_detail.html', context)


# ** edit review **
@login_required
def edit_review(request, review_id):
    """ Edit a product review """

    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product

    if not request.user.is_superuser and not request.user == review.user:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to access that page.")
        return redirect(reverse('product_detail', args=[product.id]))

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            messages.success(request, 'Review edited successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update review. Please check the form and try again.')
    else:
        form = ReviewForm(instance=review)
        messages.success(request, f'You are editing a review of {product.name}')

    template = 'products/edit_review.html'
    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }

    return render(request, template, context)


@login_required 
def delete_review(request, review_id):
    """ Delete a review """
    review = get_object_or_404(ProductReview, pk=review_id)
    product = review.product

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to access that page.")
        return redirect(reverse('product_detail', args=[product.id]))

    review.delete()

    messages.success(request, f"{review.user}'s review has now been deleted!")

    return redirect(reverse('product_detail', args=[product.id]))


@login_required 
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to access that page.")
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New product added successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please check the form and try again')
    else:
        form = ProductForm()
       
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to access that page.")
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'product edited successfully!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please check the form and try again.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required 
def delete_product(request, product_id):
    """ Delete a product from the store """

    if not request.user.is_superuser:
        messages.error(
            request,
            "Sorry, you don't have the necessary permissions to access that page.")
        return redirect(reverse('home'))
        
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} has now been deleted!')
    return redirect(reverse('products'))

