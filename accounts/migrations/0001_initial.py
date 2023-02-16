# Generated by Django 3.2 on 2023-02-16 17:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_delivery_address', models.CharField(blank=True, max_length=100, null=True)),
                ('default_town_or_city', models.CharField(blank=True, max_length=80, null=True)),
                ('default_zip_code', models.CharField(blank=True, max_length=20, null=True)),
                ('default_state', models.CharField(blank=True, max_length=100, null=True)),
                ('default_country', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
