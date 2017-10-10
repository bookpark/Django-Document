from django.db import models

__all__ = (
    'Topping',
    'Pizza',
)


class Topping(models.Model):
    pass


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
