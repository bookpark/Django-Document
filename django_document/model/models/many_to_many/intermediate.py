from django.db import models

__all__ = (
    'Idol',
    'Group',
    'Membership',
)


class Idol(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


# through_fields 사용
class Group(models.Model):
    name = models.CharField(max_length=30)
    debut_date = models.DateField()
    members = models.ManyToManyField(
        Idol,
        through='Membership',
        # 순서 중요 (source 다음 target)
        # source의 의미 (group의 idol (O), idol의 group (X))
        through_fields=('group', 'idol'),
    )

    def __str__(self):
        return self.name


class Membership(models.Model):
    idol = models.ForeignKey(
        Idol,
        on_delete=models.CASCADE,
        related_name='membership_set',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
    )
    # recommender = models.ForeignKey(
    #     Idol,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     related_name='recommend_membership_set',
    # )
    recommenders = models.ManyToManyField(
        Idol,
        blank=True,
        related_name='recommend_membership_set',
    )
    joined_date = models.DateField()
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.group.name} ' \
               f'{self.idol.name} ' \
               f'({self.is_active})'
