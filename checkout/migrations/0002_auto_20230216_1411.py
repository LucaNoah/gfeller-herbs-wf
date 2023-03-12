# Generated by Django 3.2 on 2023-02-16 14:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="delivery_address1",
            new_name="delivery_address",
        ),
        migrations.RemoveField(
            model_name="order",
            name="delivery_address2",
        ),
        migrations.AddField(
            model_name="order",
            name="town_or_city",
            field=models.CharField(default="Town or City", max_length=80),
        ),
    ]
