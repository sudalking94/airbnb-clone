# Generated by Django 3.1.7 on 2021-03-31 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210331_2025'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email_secret',
            field=models.CharField(blank=True, default='', max_length=20),
        ),
    ]
