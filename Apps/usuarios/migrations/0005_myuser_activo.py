# Generated by Django 2.2.5 on 2019-10-04 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20191002_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]