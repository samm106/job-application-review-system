# Generated by Django 3.2.15 on 2022-09-15 11:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidateName', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=5000, null=True)),
                ('positionAppliedFor', models.CharField(max_length=100)),
                ('experience', models.IntegerField(validators=[django.core.validators.MaxValueValidator(30), django.core.validators.MinValueValidator(0)])),
                ('phoneNumber', models.IntegerField(validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1000000000)])),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
