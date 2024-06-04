from django.urls import path
from videos import views

urlpatterns = [
    path("", views.video_index, name="video_index"),
    path("<int:pk>/", views.video_detail, name="video_detail"),
    path("myvideos/", views.my_videos, name="my_videos")
]