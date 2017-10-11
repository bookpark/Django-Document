from django.contrib import admin

from .models import (
    Manufacturer, Car, User,
    Person,
    Fruit,
    Topping, Pizza,
    FacebookUser, InstagramUser,
    Idol, Group, Membership,
    Place, Restaurant, Waiter)

admin.site.register(Person)
admin.site.register(Fruit)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(Idol)
admin.site.register(Group)
admin.site.register(Membership)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)