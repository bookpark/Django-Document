from django.db import models

__all__ = (
    'Place',
    'Restaurant',
    'Supplier',
)


class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Restaurant(Place):
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} Restaurant'


class Supplier(Place):
    # place_ptr = models.OneToOneField(Place)
    supply_places = models.ManyToManyField(
        Place,
        related_name='supply_place_set',
        related_query_name='supply_place',
    )
