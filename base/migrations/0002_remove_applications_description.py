# Generated by Django 3.2.15 on 2022-09-15 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='description',
        ),
    ]
