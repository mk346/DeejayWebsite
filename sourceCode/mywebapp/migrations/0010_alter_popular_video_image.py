# Generated by Django 3.2.4 on 2021-07-24 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0009_popular_video_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popular',
            name='video_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]