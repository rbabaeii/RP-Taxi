# Generated by Django 4.1.2 on 2022-12-04 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_traveladdress_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requestcar',
            options={'verbose_name': 'درخواست ماشین', 'verbose_name_plural': 'درخواست های ماشین'},
        ),
        migrations.AlterModelOptions(
            name='traveladdress',
            options={'verbose_name': ' آدرس های خاص', 'verbose_name_plural': '  آدرس های خاص'},
        ),
    ]
