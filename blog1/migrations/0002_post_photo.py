# Generated by Django 2.2.9 on 2020-01-20 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
