# Generated by Django 3.2.9 on 2021-12-08 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_post_author'),
        ('comments', '0002_alter_comment_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post_title',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to='webpages.post'),
        ),
    ]