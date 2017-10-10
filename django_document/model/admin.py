from django.contrib import admin

from .models import (
    Manufacturer,
    Car,
    User,
    Person,
    Fruit,
)
from .models.many_to_many import (
    Topping,
    Pizza,
    FacebookUser,
    InstagramUser,
)

admin.site.register(Person)
admin.site.register(Fruit)
admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(User)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
