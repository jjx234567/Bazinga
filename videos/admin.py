from django.contrib import admin
from videos.models import Video

class VideoAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Video, VideoAdmin)