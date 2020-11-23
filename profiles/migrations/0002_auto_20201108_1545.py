# Generated by Django 3.1.3 on 2020-11-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=200, unique=True, verbose_name='email address'),
        ),
    ]
