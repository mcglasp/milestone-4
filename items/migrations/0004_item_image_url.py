# Generated by Django 3.2.5 on 2021-08-17 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20210816_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
