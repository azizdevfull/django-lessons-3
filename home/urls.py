from django.urls import path

from . import views

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('user/<int:user_id>/orders/', views.user_orders, name='user_orders'),
    path('order/<int:order_id>/products/', views.order_products, name='order_products'),
]
