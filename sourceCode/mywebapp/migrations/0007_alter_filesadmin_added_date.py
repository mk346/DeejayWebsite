# Generated by Django 3.2.4 on 2021-07-22 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebapp', '0006_filesadmin_added_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesadmin',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
