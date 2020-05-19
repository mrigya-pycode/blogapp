# Generated by Django 3.0.6 on 2020-05-16 07:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='bloger_pic',
            field=models.FileField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger_author',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 5, 16, 12, 52, 5, 23199)),
        ),
    ]
