# Generated by Django 3.2 on 2021-05-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20210529_1500'),
    ]

    operations = [
        migrations.AddField(
            model_name='hrproject',
            name='img',
            field=models.ImageField(default='profile_pics/front.jpg', upload_to='profile_pics'),
        ),
        migrations.AlterModelTable(
            name='hrproject',
            table='home_hrproject',
        ),
    ]
