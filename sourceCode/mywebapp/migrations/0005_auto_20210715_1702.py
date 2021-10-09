# Generated by Django 3.2.4 on 2021-07-15 14:02

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0004_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-added_date']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='video',
            new_name='video_url',
        ),
        migrations.AddField(
            model_name='item',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default=datetime.datetime(2021, 7, 15, 14, 2, 41, 565581, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]