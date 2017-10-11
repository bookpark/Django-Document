from django.contrib import admin

from .models import Student, Teacher, School

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
