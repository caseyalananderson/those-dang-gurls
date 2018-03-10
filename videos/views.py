from django.shortcuts import render

from .models import Video


# Create your views here.
def index(request):
    """
    Main index that displays blog post
    :param request:
    :return:
    """

    videos = Video.objects.all()

    context = {
        'videos': videos,
    }

    return render(request, 'videos/videos.html', context)