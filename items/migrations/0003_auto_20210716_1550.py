# Generated by Django 3.2.5 on 2021-07-16 15:50

from django.db import migrations, models
import items.utils


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_auto_20210716_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(blank=True, default=items.utils.create_new_sku, max_length=254, null=True),
        ),
    ]
