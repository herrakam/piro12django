from django.db import models

# Create your models here.

class item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)#추가될 때에 자동 저장
    updated_at = models.DateTimeField(auto_now=True)

