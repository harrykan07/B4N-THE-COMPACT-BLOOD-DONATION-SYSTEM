# Generated by Django 3.2 on 2021-05-07 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0005_auto_20210507_1929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donorlist',
            name='home_address',
        ),
    ]
