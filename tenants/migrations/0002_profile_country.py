# Generated by Django 5.0 on 2023-12-25 08:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tenants", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="country",
            field=models.CharField(default="India", max_length=50),
        ),
    ]