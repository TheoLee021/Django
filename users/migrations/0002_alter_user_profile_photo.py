# Generated by Django 5.1.5 on 2025-01-24 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(blank=True, upload_to=""),
        ),
    ]
