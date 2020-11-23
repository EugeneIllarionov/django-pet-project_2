# Generated by Django 3.1.3 on 2020-11-22 20:25

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31, unique=True),
        ),
    ]
