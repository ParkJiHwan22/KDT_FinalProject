# Generated by Django 3.2.18 on 2023-05-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_planets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='plan',
            field=models.CharField(choices=[('Free', 'Free'), ('Premium', 'Primium')], default='Free', max_length=10),
        ),
    ]
