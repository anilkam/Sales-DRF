from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(blank=True, default='', max_length=300)
    price = models.FloatField(validators=[MinValueValidator(0.1)])

    def __str__(self):
        return self.name


class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])

    @property
    def sub_total(self):
        return self.product.price * self.quantity

    class Meta:
        unique_together = (("user", "product"),)
