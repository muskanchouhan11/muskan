# Generated by Django 3.2 on 2021-05-16 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_hrproject_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='hrproject',
            table='home_hrproject',
        ),
    ]