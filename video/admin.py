from django.contrib import admin
from .models import VideoContainer, VideoFile, Subtitle, Localizator, VideoCategory

admin.site.register(VideoContainer)
admin.site.register(VideoFile)
admin.site.register(Subtitle)
admin.site.register(Localizator)
admin.site.register(VideoCategory)
