# Generated by Django 3.1.6 on 2021-06-10 13:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banker', '0005_auto_20210610_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='dob',
            field=models.DateTimeField(default=datetime.date(2021, 6, 10)),
        ),
    ]