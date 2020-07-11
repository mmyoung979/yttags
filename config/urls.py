# Django imports
from django.urls import path, include
from django.contrib import admin

# Project imports
from yttags.tags import urls as tags
from yttags.keywords import urls as keywords

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(tags)),
    path('', include(keywords)),
]
