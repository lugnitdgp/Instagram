# Generated by Django 2.0.2 on 2020-01-25 09:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0013_auto_20200124_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 25, 9, 3, 2, 296925, tzinfo=utc)),
        ),
    ]
