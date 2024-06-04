from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# projects/views.py

from videos.models import Video

@login_required
def video_index(request):
    bazingas = Video.objects.all()
    context = {
        "videos": bazingas
    }
    return render(request, "videos/video_index.html", context)
@login_required
def video_detail(request, pk):
    bazingas = Video.objects.get(pk=pk)
    context = {
        "video": bazingas
    }
    return render(request, "videos/video_detail.html", context)
@login_required
def my_videos(request):
    bazingas = Video.objects.filter(publisher=request.user)
    context = {
        "videos": bazingas
    }
    return render(request, "videos/my_videos.html", context)