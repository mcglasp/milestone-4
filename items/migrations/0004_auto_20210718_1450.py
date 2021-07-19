# Generated by Django 3.2.5 on 2021-07-18 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210716_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='age_range',
        ),
        migrations.AddField(
            model_name='item',
            name='age_range',
            field=models.ManyToManyField(to='items.Age_range'),
        ),
        migrations.RemoveField(
            model_name='item',
            name='author',
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.ManyToManyField(to='items.Author'),
        ),
    ]
