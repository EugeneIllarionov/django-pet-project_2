# Generated by Django 3.1.3 on 2020-11-09 18:03

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201109_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to='media'),
        ),
    ]
