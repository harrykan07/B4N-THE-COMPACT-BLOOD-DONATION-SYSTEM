# Generated by Django 3.2 on 2021-05-08 08:42

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_points_requestedrecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestedrecord',
            name='addr',
        ),
        migrations.RemoveField(
            model_name='requestedrecord',
            name='city',
        ),
        migrations.RemoveField(
            model_name='requestedrecord',
            name='date',
        ),
        migrations.AddField(
            model_name='requestedrecord',
            name='address',
            field=mapbox_location_field.models.AddressAutoHiddenField(blank=True, map_id='map', null=True),
        ),
        migrations.AddField(
            model_name='requestedrecord',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('a+', 'A+'), ('a-', 'A-'), ('b+', 'B+'), ('b-', 'B-'), ('o+', 'O+'), ('o-', 'O-'), ('ab+', 'AB+'), ('ab-', 'AB-')], max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='requestedrecord',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='requestedrecord',
            name='location',
            field=mapbox_location_field.models.LocationField(blank=True, map_attrs={'center': (17.031645, 51.106715), 'style': 'mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72'}, null=True),
        ),
    ]
