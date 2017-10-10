from django.contrib import admin

from .models import Manufacturer, Car, User, Person, Fruit, Topping, Pizza

admin.site.register(Person)
admin.site.register(Fruit)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Topping)
admin.site.register(Pizza)
