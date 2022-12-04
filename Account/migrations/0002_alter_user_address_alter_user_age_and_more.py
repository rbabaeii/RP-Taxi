# Generated by Django 4.1.2 on 2022-11-21 10:36

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Address',
            field=models.CharField(blank=True, max_length=100, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Age',
            field=models.IntegerField(blank=True, default=0, verbose_name='سن'),
        ),
        migrations.AlterField(
            model_name='user',
            name='mellicode',
            field=models.CharField(blank=True, max_length=10, verbose_name='کدملی'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default=None, max_length=128, null=True, region=None, unique=True, verbose_name='شماره تلفن'),
        ),
    ]
