from django.db import models

__all__ = (
    'Person',
)


# 튜플을 써서 필드에 쓰일 Choices 생성; DB에선 왼쪽에 정의 된 값만 보여지고 유저에겐 오른쪽에 있는 값이 보여짐
class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)
