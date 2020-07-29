# Django imports
from django.shortcuts import render

# 3rd party imports
from rest_framework import serializers

# Project imports
from .forms import TagsForm
from .utils import get_video_data, youtube_search
from .models import Video
from yttags.frontend.api.serializers import VideoSerializer


# Homepage
def home(request):
    context = {'form': TagsForm}
    return render(request, 'home.html', context)


# About page
def about(request):
    return render(request, 'about.html')


# Load search
def tags(request):
    # Form to determine YouTube URL
    form = TagsForm(request.POST or None)

    # Load form
    context = {'form': form}

    # If form was submitted, load tags
    if request.method == 'POST':
        if form.is_valid():
            url = form.cleaned_data.get('url')

            # Check desktop and mobile URL patterns
            if url.find('v=') != -1:
                video_id = url[url.find('v=') + 2::]
            elif url.find('.be/') != -1:
                video_id = url[url.find('.be/') + 4::]
            else:
                video_id = 'The URL may not have been entered properly'

            # Filter through video data for output
            try:
                # Get video
                video = get_video_data(video_id)
                video_object = Video()
                video_object.youtube_id = video_id
                video_object.save()
                context['title'] = video['title']
                context['thumbnail'] = video['thumbnail']
                context['tags'] = video['tags']

            # Error handling
            except ConnectionError as e:
                context['error'] = 'Too many attempts. Please try again in a few minutes.'
            except IndexError as e:
                context['error'] = 'Please enter a YouTube video link'

    # Display HTML page
    return render(request, 'tags.html', context)
