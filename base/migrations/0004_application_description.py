# Generated by Django 3.2.15 on 2022-09-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_rename_applications_application'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
