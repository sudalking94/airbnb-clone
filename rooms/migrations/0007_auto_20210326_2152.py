# Generated by Django 3.1.7 on 2021-03-26 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0006_auto_20210326_2150"),
    ]

    operations = [
        migrations.AlterField(
            model_name="room",
            name="amenities",
            field=models.ManyToManyField(
                blank=True, related_name="banana", to="rooms.Amenity"
            ),
        ),
    ]
