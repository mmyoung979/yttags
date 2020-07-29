# 3rd party imports
from rest_framework import serializers


class VideoSerializer(serializers.Serializer):
    youtube_id = serializers.CharField(max_length=150)
