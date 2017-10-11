from django.db import models

__all__ = (
    'FacebookUser',
)


# 방향성이 없고 서로 대칭 관계를 갖는다 (기본값)
class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField(
        'self',
        blank=True,
    )

    def __str__(self):
        return self.name
