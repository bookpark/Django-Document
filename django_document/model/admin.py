from django.contrib import admin

from model.models import Manufacturer, Car, User

admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(User)