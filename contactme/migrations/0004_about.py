# Generated by Django 3.2.9 on 2021-12-11 05:45

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactme', '0003_myinfo_website_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_photo', models.ImageField(upload_to='media/about/%Y/%m')),
                ('about_me', ckeditor.fields.RichTextField()),
                ('created_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
