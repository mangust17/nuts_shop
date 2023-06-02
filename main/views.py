from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from . import forms
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


def main_page(request):
    product = Product.objects.all()
    return render(request, 'main_page.html', {'title': 'Главная страница сайта', 'product': product})


def create_us(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Такой email уже существует")
                return redirect('create_us')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Это имя уже занято")
                return redirect('create_us')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                profile = Profile.objects.create(user=user)
                profile.save()
                messages.success(request, 'Пользователь создан!')
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request, "Пароли не совпадают")
            return redirect('create_us')
    else:
        return render(request, 'main/create_us.html')


def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Введенные данные не верны")
            return redirect('sign_in')
    else:
        return render(request, 'main/signin.html')


def log_out(request):
    auth.logout(request)
    return redirect('/')


def search(request):
    if request.method == 'POST':
        searched_product = request.POST.get('searched', '')
        products = Product.objects.filter(product_name__icontains=searched_product)
        if products:
            return render(request, 'search.html', {'searched': searched_product, 'products': products})
        else:
            return render(request, 'search.html', {'searched': searched_product, 'error': 'No results found'})
    else:
        return render(request, 'search.html')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Product, pk=pk)

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_view')


