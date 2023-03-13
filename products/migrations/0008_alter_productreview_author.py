# Generated by Django 3.2 on 2023-03-13 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0007_rename_category_productreview_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productreview",
            name="author",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
