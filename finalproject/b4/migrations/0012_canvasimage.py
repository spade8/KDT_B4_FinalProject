# Generated by Django 4.0.3 on 2023-01-14 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b4', '0011_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='CanvasImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='origin')),
            ],
        ),
    ]