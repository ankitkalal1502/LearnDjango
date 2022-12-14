# Generated by Django 4.1 on 2022-08-08 06:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_cart_user_deal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(message='phone number should exactly be in 10 digits', regex='^\\d{10}$')])),
                ('query', models.TextField()),
            ],
        ),
    ]
