# Generated by Django 4.2.16 on 2024-11-30 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0004_community'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='date',
        ),
    ]
