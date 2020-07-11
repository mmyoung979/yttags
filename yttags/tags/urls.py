# Django imports
from django.urls import path

# Project imports
from . import views


# URLs
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('tags/', views.tags, name='tags'),
]
