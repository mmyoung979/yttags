# Django imports
from django.contrib import admin

# Project imports
from .models import Video


# Register Video model
@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    pass
