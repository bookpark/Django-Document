from django.db import models

__all__ = (
    'Topping',
    'Pizza',
)


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    toppings = models.ManyToManyField(Topping)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
