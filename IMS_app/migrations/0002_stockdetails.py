# Generated by Django 4.2.16 on 2024-11-27 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IMS_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=120)),
                ('amount', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('dateAdded', models.DateField()),
                ('supplier', models.CharField(max_length=120)),
                ('supplierNo', models.IntegerField()),
                ('supplierEmail', models.EmailField(max_length=254)),
                ('image', models.ImageField(upload_to='stock/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
