# Generated by Django 3.2 on 2021-05-30 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20210530_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrproject',
            name='img',
            field=models.ImageField(default='front.jpg', upload_to='profile_pics'),
        ),
    ]