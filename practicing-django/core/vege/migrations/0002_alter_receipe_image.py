# Generated by Django 5.0.7 on 2024-07-13 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipe',
            name='image',
            field=models.ImageField(upload_to='./receipes'),
        ),
    ]
