from django.db import models

__all__ = (
    'Car',
    'Manufacturer',
    'User',
)


# 만약 아직 정의되지 않은 ForeignKey를 정의하고 싶다면 참조하는 클래스를 문자열로 넣어준다 (문자열이기 때문에 rename 할 때 같이 바뀌지 않는다)
class Car(models.Model):
    # 제조사가 사라지면 차종도 사라진다
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f'{self.manufacturer.name} - {self.name}'


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# 동등한 유저일 때 관계를 가지는 경우 (Recursive relationships)
class User(models.Model):
    name = models.CharField(max_length=30)
    # 배우자가 없어져도 자신은 없어지지 않는다 (on_delete=models.SET_NULL)
    spouse = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.spouse and self.spouse.pk == self.pk:
            self.spouse = None
        super(User, self).save(*args, **kwargs)
