# Generated by Django 3.1.6 on 2021-06-10 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banker', '0003_userinfo_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]