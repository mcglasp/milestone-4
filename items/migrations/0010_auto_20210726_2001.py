# Generated by Django 3.2.5 on 2021-07-26 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0009_alter_item_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='discounted_price',
        ),
        migrations.AlterField(
            model_name='item',
            name='discount',
            field=models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=2, null=True),
        ),
    ]
