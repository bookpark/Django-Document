from django.db import models

__all__ = (
    'Fruit',
)


# Fruit 'name'을 Primary Key로 지정
class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
