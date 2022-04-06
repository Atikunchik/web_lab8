from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    price = models.FloatField(
        default=0
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    count = models.IntegerField(
        default=0
    )
    is_active = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'{self.name} - {self.price}'


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )