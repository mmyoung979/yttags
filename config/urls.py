# Django imports
from django.urls import path, include
from django.contrib import admin

# Project imports
from yttags.frontend import urls as frontend
from yttags.frontend.api import urls as api
from yttags.tags import urls as tags
from yttags.keywords import urls as keywords

# URLs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(tags)),
    path('', include(keywords)),
    path('', include(frontend)),
    path('api/', include(api))
]
