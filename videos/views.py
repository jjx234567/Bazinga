from django.shortcuts import render

# Create your views here.

# projects/views.py

from videos.models import Video

def video_index(request):
    bazingas = Video.objects.all()
    context = {
        "videos": bazingas
    }
    return render(request, "videos/video_index.html", context)

def video_detail(request, pk):
    bazingas = Video.objects.get(pk=pk)
    context = {
        "video": bazingas
    }
    return render(request, "videos/video_detail.html", context)