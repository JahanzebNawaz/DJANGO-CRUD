# Generated by Django 2.2.7 on 2019-11-07 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0003_auto_20191107_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='img/user.jpg', upload_to='media', verbose_name='Profile Pic'),
        ),
    ]
