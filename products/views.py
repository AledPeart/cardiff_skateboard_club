from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from django.core.paginator import Paginator 
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand, ProductReview
from profiles.models import UserProfile
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all CSC products """

    products = Product.objects.all()
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
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)


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
        # 'product_list': product_list,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

# Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', 3)
        review_text = request.POST.get('review_text', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, review_text=review_text)

        messages.success(request, f"You have succesfully added a product review!")

        return redirect(reverse('product_detail', args=[product.id]))

    context = {
         'product': product,
    }

    return render(request, 'products/product_detail.html', context)

@login_required 
def delete_review(request, review_id):
    """ Delete a review from the product store """

    review = get_object_or_404(ProductReview, pk=review_id)
    review_owner = review.user
    product = review.product

    if not request.user.is_superuser or request.user == review.user:
        messages.error(request, "Sorry, you don't have the necessary permissions to access that page.")
        return redirect(reverse('home'))

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



# @login_required
# def save_review(request, product_id):
#     """ Add and save a product review """

#     product = get_object_or_404(Product, pk=product_id)
#     profile = get_object_or_404(UserProfile, user_id=request.user)
  
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             form = ReviewForm(request.POST)
#             reviews = product.reviews.all()

#             if reviews.filter(user=request.user).exists():
#                 messages.info(
#                     request, f"You've already reviewed {product.name}")
#                 return redirect(reverse('product_detail', args=[product.id]))

#             if form.is_valid():
#                 review = form.save(commit=False)
#                 review.product = product
#                 review.user = request.user
#                 # Check whether line items related to user include the product
#                 if OrderLineItem.objects.filter(
#                     order__user_profile=profile).filter(
#                         product=product).exists():
#                     review.verified_purchase = True

#                 review.save()
#                 if review.verified_purchase:
#                     messages.info(
#                         request,
#                         'Thanks for the review - 5 points to you!')
#                 else:
#                     messages.info(
#                         request,
#                         'Thanks for the review!')

#                 return redirect(reverse('product_detail', args=[product.id]))
#             else:
#                 messages.error(
#                     request,
#                     "Failed to add review - please check form and try again")

#     context = {
#         'form': form,
#         'profile': profile,
#     }

#     return render(request, context)






    # product = get_object_or_404(Product, pk=product_id)
    # user = request.user
    # review = ProductReview.objects.create(
	# 	user=user,
	# 	product=product,
	# 	review_text=request.POST['review_text'],
	# 	review_rating=request.POST['review_rating'],
	# 	)
    # data = {
	# 	'user': user.username,
	# 	'review_text': request.POST['review_text'],
	# 	'review_rating': request.POST['review_rating']
	# }

	# # Fetch avg rating for reviews
    # avg_reviews = ProductReview.objects.filter(product=product).aggregate(avg_rating=Avg('review_rating'))
	# # End

    # return JsonResponse({'bool': True, 'data': data,'avg_reviews': avg_reviews})
