from django.db import models
from django.conf import settings
# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)#추가될 때에 자동 저장
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_PASSWORD_VALIDATORS,on_delete=models.CASCADE)
