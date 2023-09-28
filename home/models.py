from django.db import models
from django.contrib.auth.models import User

class Product(models.Model) :
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image1 = models.ImageField(upload_to='Product')
    image2 = models.ImageField(upload_to='Product')


    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name