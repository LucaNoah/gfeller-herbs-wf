# Generated by Django 3.2 on 2023-03-13 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_has_quantity_product_has_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_weight',
        ),
    ]