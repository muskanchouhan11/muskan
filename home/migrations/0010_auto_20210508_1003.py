# Generated by Django 3.2 on 2021-05-08 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_register_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Register',
            new_name='Hrproject',
        ),
        migrations.AlterModelTable(
            name='hrproject',
            table=None,
        ),
    ]
