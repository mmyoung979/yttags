# Django imports
from django.shortcuts import render

# Python imports
from concurrent.futures import ThreadPoolExecutor

# Project imports
from .forms import KeywordsForm
from yttags.tags.utils import youtube_search, get_video_data


# Tag object
class Tag:
    def __init__(self, tag, count):
        self.tag = tag
        self.count = count

    def get_count(self):
        return self.count


def keywords(request):
    # Form to determine YouTube Search
    form = KeywordsForm(request.POST or None)

    # Load form
    context = {'form': form}

    if request.method == 'POST':
        if form.is_valid():
            # Search
            keywords = form.cleaned_data.get('keywords')
            max_results = 20
            context['title'] = keywords
            video_ids = youtube_search(keywords, max_results)

            # Add all tags to master list
            all_tags = []
            with ThreadPoolExecutor(max_workers=4) as executor:
                for video in executor.map(get_video_data, video_ids):
                    for tag in video['tags']:
                        all_tags.append(tag.lower())

            # Create list of Tag objects
            tags = []
            for tag in sorted(list(set(all_tags))):
                tags.append(Tag(tag, all_tags.count(tag)))

            # Output Tag objects
            context['tags'] = sorted(tags, key=lambda tag: tag.count, reverse=True)

    # Display results
    return render(request, 'keywords.html', context)
