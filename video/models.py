from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import m2m_changed
from django.dispatch import receiver


class VideoCategory(models.Model):
    name = models.CharField(max_length=200)
    image_url_ending = models.CharField(max_length=300)
    parent_categories = models.ManyToManyField("self", related_name="subcategories", symmetrical=False, blank=True)

    def __str__(self):
        return self.name


class Localizator(models.Model):
    nickname = models.CharField(max_length=200)

    def __str__(self):
        return self.nickname


class VideoContainer(models.Model):
    name = models.CharField(max_length=200)

    categories = models.ManyToManyField(VideoCategory, related_name="videos", blank=True)
    date = models.DateTimeField(null=True, blank=True)

    short_description = models.TextField(max_length=2000, blank=True, null=True)

    full_description = models.TextField(blank=True, null=True)

    translation_commentaries = models.TextField(null=True, blank=True)
    image_url_ending = models.CharField(max_length=300)

    translators = models.ManyToManyField(Localizator, related_name="translated_videos", blank=True)
    editors = models.ManyToManyField(Localizator, related_name="edited_videos", blank=True)

    def __str__(self):
        return "{} -> {}".format(self.categories.first().name, self.name)


class Subtitle(models.Model):
    parent_video = models.ForeignKey(VideoContainer, on_delete=models.CASCADE, related_name="subtitles")
    language = models.CharField(max_length=300)
    url_ending = models.CharField(max_length=1000)

    def __str__(self):
        return "{}: {}".format(str(self.parent_video), self.language)


class VideoFile(models.Model):
    parent_video_container = models.ForeignKey(VideoContainer, on_delete=models.CASCADE, related_name="video_files")
    video_as_track_name = models.CharField(max_length=100)
    url_ending = models.CharField(max_length=1000)

    def __str__(self):
        return "{}: {}".format(self.parent_video_container, self.video_as_track_name)


@receiver(m2m_changed, sender=VideoCategory.parent_categories.through)
def prevent_duplicate_tags_from_group(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_add':
        if instance.pk in pk_set:
            raise ValidationError({'parent_categories': 'Cant add yourself'})
