# Generated by Django 3.2 on 2021-05-10 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dreg', '0008_alter_donorlist_last_donate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donorlist',
            name='last_donate_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
