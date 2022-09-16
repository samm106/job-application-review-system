import imp
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('candidate/<str:id>', views.candidate, name='candidate'),
    path('create-candidate/', views.createCandidate, name="create-candidate"),
    path('update-candidate/<str:id>', views.updateCandidate, name='update-candidate'),
    path('delete-candidate/<str:id>', views.deleteCandidate, name='delete-candidate'),
]