# Django imports
from django.urls import path

# Project imports
from . import views


# URLs
urlpatterns = [
    path('keywords', views.keywords, name='keywords'),
]
