# Generated by Django 4.1.5 on 2023-01-16 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("b4", "0017_alter_photos_background_color"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photos",
            name="background_color",
            field=models.CharField(default="", max_length=10),
        ),
    ]