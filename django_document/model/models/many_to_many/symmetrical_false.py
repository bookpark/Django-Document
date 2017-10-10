from django.db import models

__all__ = (
    'InstagramUser',
)


# 방향성이 생기고 서로 비대칭 관계를 갖는다
class InstagramUser(models.Model):
    name = models.CharField(max_length=30)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)

    def __str__(self):
        return self.name
