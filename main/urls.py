from django.urls import path
from . import views
from .views import ProductDetailView


urlpatterns = [
    path('', views.main_page, name='home'),
    path('about', views.about, name='about'),
    path('account', views.account, name='account'),
    path('create_us', views.create_us, name='create_us'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('log_out', views.log_out, name='log_out'),
    path('search', views.search, name='search'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart', views.cart, name='cart'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout_order', views.checkout, name='checkout')
]
