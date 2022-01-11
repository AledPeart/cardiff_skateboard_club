from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product


# Create your views here.

def view_bag(request):
    """ View to return bag contents page """
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Very nice! You now have {bag[item_id]} of {product.name} in your bag. Nice!')
    else:
        bag[item_id] = quantity
        messages.success(request, f'You have added {product.name} to your bag. Nice!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust the quantity of the specified product in the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
        messages.success(request, f'You now have {bag[item_id]} of {product.name} in your bag. Nice!')
    else:
        bag.pop(item_id)
        
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


# def remove_from_bag(request, item_id):
#     """Remove the item from the shopping bag"""

#     try:
#         product = get_object_or_404(Product, pk=item_id)
#         bag = request.session.get('bag', {})
    
#         bag.pop(item_id)
#         messages.success(request, f'{product.name} was removed from your bag')

#         request.session['bag'] = bag
#         return redirect(reverse('view_bag'))
        
#     except Exception as e:
#         messages.error(request, f'Error removing item: {e}')
#         return HttpResponse(status=500)
 
def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})

        
    
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)



