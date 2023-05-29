from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='home'),
    path('create_us', views.create_us, name='create_us'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('log_out', views.log_out, name='log_out'),
    path('search', views.search, name='search'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]