# Generated by Django 4.2.16 on 2024-11-30 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0005_remove_community_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='post',
            field=models.TextField(max_length=150),
        ),
    ]