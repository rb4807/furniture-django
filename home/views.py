from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import CartItem,Product
from django.contrib.auth.decorators import login_required

# home

def home(request):
    return render(request, 'home/index.html')

# products

def product(request):
    product = Product.objects.all()
    return render(request, 'home/product.html', {'product' : product})

# cart
# add to cart
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user, ordered=False)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('cart')

# cart

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user, ordered=False)
    context = {'cart_items': cart_items}
    return render(request, 'home/cart.html', context)

# increase quantity

@login_required
def increase_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

# decrease quantity

@login_required
def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return redirect('cart')

# remove from cart

@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart')

