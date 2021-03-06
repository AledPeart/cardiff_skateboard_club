from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history,
         name='order_history'),
    path('wishlist/add_to_wishlist/<int:product_id>/', views.add_to_wishlist,
         name='add_to_wishlist'),
    path('profile/user_wishlist/', views.user_wishlist,
         name='user_wishlist'),
    path('profile/order_summary/', views.order_summary,
         name='order_summary'),
    path('profile/user_details/', views.user_details,
         name='user_details'),
]
