# Generated by Django 3.2.18 on 2023-04-20 08:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0003_auto_20230420_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='like_users',
            field=models.ManyToManyField(related_name='like_comments', to=settings.AUTH_USER_MODEL),
        ),
    ]