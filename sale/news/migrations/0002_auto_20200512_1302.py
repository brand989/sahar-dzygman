# Generated by Django 3.0.5 on 2020-05-12 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='News',
        ),
    ]
