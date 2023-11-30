from django.db import models

from constants import STARS


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    stars = models.IntegerField(choices=STARS, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', null=True)

    def __str__(self):
        return f"Review for {self.product.title}"

