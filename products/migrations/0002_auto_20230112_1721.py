# Generated by Django 3.2 on 2023-01-12 17:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="rating",
        ),
        migrations.AlterField(
            model_name="product",
            name="image_url",
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
