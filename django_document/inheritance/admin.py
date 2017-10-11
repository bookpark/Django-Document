from django.contrib import admin

from .models import (
    Student, Teacher, School,
    Place, Restaurant,
    Supplier, Champion)


# Admin 페이지 커스터마이징
class ChampionAdmin(admin.ModelAdmin):
    list_display = ('name', 'champion_type', 'rank')
    list_editable = ('rank',)


admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Supplier)
admin.site.register(Champion, ChampionAdmin)