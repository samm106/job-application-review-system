from distutils.command.upload import upload
from pickle import TRUE
from pyexpat import model
from venv import create
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class application(models.Model):
    # id = models.UUIDField()
    candidateName = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    positionAppliedFor = models.CharField(max_length=100)
    experience = models.IntegerField(validators=[MaxValueValidator(30), MinValueValidator(0)])
    phoneNumber = models.IntegerField(validators=[MaxValueValidator(9999999999), MinValueValidator(1000000000)])
    city = models.CharField(max_length=100)
    state= models.CharField(max_length=100)
    resume = models.FileField(upload_to='pdfs/', default='settings.MEDIA_ROOT/pdfs/sameer saxena.pdf')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.candidateName