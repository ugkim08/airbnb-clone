# Generated by Django 2.2.5 on 2020-08-31 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_auto_20200831_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='amenites',
            new_name='amenities',
        ),
    ]
