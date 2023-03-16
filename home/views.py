# views.py
from django.shortcuts import render
from .models import User, Order

def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def user_orders(request, user_id):
    user = User.objects.get(id=user_id)
    orders = user.orders.all()
    return render(request, 'user_orders.html', {'user': user, 'orders': orders})

def order_products(request, order_id):
    order = Order.objects.get(id=order_id)
    products = order.products.all()
    return render(request, 'order_products.html', {'order': order, 'products': products})
