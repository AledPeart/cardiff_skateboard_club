from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile, Product
from .forms import UserProfileForm

from checkout.models import Order



@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please check the form and try again.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def user_details(request):
    """ Display the user details page. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please check the form and try again.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/user_details.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_summary(request):
    """ Display the user's previous order summary """

    
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all()


    template = 'profiles/order_summary.html'
    context = {
        'orders': orders,
        'from_profile': True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Display the user's previous orders """

    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def user_wishlist(request):
    """ A view to display the user's wishlist """

    profile = get_object_or_404(UserProfile, user=request.user)
    products = profile.wishlist.all()
    template = 'profiles/user_wishlist.html'

    context = {
        'products': products,
        'profile': profile,
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, product_id):
    """ Adding/removing items from the user's wishlist """

    product = get_object_or_404(Product, pk=product_id)
    profile = get_object_or_404(UserProfile, user=request.user)
    print (profile.wishlist.all)
# code taken from tutor support session with @igor_ci
    if product in profile.wishlist.all():
        profile.wishlist.remove(product)
        messages.success(request, f'{product.name} was removed from your wishlist')
    else:
        profile.wishlist.add(product)
        messages.success(request, f'You have added {product.name} to your wishlist')
        
    return HttpResponseRedirect(request.META["HTTP_REFERER"])



