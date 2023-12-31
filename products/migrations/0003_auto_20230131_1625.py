# Generated by Django 3.2 on 2023-01-31 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_auto_20230112_1721"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.AddField(
            model_name="product",
            name="has_quantity",
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
