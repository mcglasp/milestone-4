# Generated by Django 3.2.5 on 2021-07-19 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_auto_20210718_1450'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='genre',
        ),
        migrations.AddField(
            model_name='item',
            name='genre',
            field=models.ManyToManyField(to='items.Genre'),
        ),
    ]
