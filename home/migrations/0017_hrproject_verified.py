# Generated by Django 3.2 on 2021-05-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_hrproject_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrproject',
            name='verified',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
