# Generated by Django 2.2.1 on 2019-06-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writers', '0002_auto_20190527_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
