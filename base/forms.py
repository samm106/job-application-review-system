from dataclasses import field
from django.forms import ModelForm
from .models import application

class ApplicationForm(ModelForm):
    class Meta:
        model = application
        fields = '__all__'