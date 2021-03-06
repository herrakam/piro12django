from django.db import models
from mysite.utils import uuid_upload_to
from django.urls import reverse
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)#추가될 때에 자동 저장
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<{}> {}'.format(self.pk, self.name)

    def get_absolute_url(self):
        return reverse('shop:item_detail', args=[self.pk])

