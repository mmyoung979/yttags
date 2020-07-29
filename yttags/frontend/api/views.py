# Django imports
from django.shortcuts import render

# 3rd party imports
from rest_framework import viewsets, permissions

# Project imports
from .serializers import VideoSerializer
from yttags.tags.models import Video


class TagsViewset(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VideoSerializer
