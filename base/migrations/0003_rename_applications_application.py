# Generated by Django 3.2.15 on 2022-09-15 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_remove_applications_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='applications',
            new_name='application',
        ),
    ]
