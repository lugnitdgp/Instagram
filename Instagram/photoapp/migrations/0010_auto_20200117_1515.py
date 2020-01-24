# Generated by Django 2.0.2 on 2020-01-17 15:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photoapp', '0009_auto_20191226_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 17, 15, 15, 25, 259184, tzinfo=utc)),
        ),
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='postlikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
