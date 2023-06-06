from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')

    def __str__(self):
        return self.user.name


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.TextField()
    product_bio = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('home')

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.user.name}'s CartItem: {self.product}"
