# Generated by Django 3.1.3 on 2020-11-11 08:19

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20201111_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(default='default_avatar.jpg', upload_to='avatars'),
        ),
    ]
