from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import Http404
from .models import VideoContainer, VideoCategory  # , VideoToken
from .playerjs_base64 import pjs_b64_encrypt


def get_video_string(video_container):
    video_files = video_container.video_files.all()
    if len(video_files) > 1:
        video_string = ";".join(["{{{0}}}{1}{2}".format(video_file.video_as_track_name,
                                                                "/video/get-file?name=",
                                                                video_file.url_ending)
                                         for video_file in video_files])
    elif len(video_files) == 1:
        video_string = "{0}{1}".format("/video/get-file?name=", video_files[0].url_ending)
    else:
        video_string = ""
    return video_string


def get_subtitle_string(video_container):
    return ",".join(["[{0}]{1}{2}".format(subtitle_file.language,
                                                     "/video/get-file?name=",
                                                     subtitle_file.url_ending)
                                for subtitle_file in video_container.subtitles.all()])


def get_poster_string(video_container):
    return "/video/get-file?name={}".format(video_container.image_url_ending)


def base_categories_list(request):
    base_categories = VideoCategory.objects.filter(parent_categories=None)
    return render(request, 'video/base_categories_list.html', {"base_categories": base_categories})


def category_detail(request, pk,
                    main_template='video/category_detail.html',
                    video_template='video/category_detail_page_video.html'):
    category = get_object_or_404(VideoCategory, pk=pk)
    subcategories = category.subcategories.all()
    videos = category.videos.filter(date__lte=timezone.now()).order_by('date')
    context = {"subcategories": subcategories, "videos": videos,
               'v_template': video_template}
    if request.is_ajax():
        main_template = video_template
    return render(request, main_template, context)


def video_detail(request, pk):
    v_container = get_object_or_404(VideoContainer, pk=pk)
    v_series_id = str(v_container)

    playlist_els = []
    category_videos = v_container.categories.first().videos.filter(date__lte=timezone.now()).order_by('date')
    for c_video in category_videos:
        v_title = str(c_video)
        v_link = get_video_string(c_video)
        v_subtitles = get_subtitle_string(c_video)
        v_poster = get_poster_string(c_video)
        playlist_els.append('{{"title": "{}", "file": "{}", '
                            '"subtitle":"{}", "poster":"{}", "id":"{}"}}'.format(v_title,
                                                                                 v_link,
                                                                                 v_subtitles,
                                                                                 v_poster,
                                                                                 v_title))
    playlist_string = "[{}]".format(",".join(playlist_els))


    translators = ", ".join(translator.nickname for translator in v_container.translators.all())
    editors = ", ".join(editor.nickname for editor in v_container.editors.all())

    final_player_string = '{{' \
                          '"id": "player", ' \
                          '"file": {0}, ' \
                          '"default_subtitle": "Без субтитров", ' \
                          '"default_audio": "Русский", ' \
                          '"plstart": "{1}" ' \
                          '}}'.format(playlist_string, v_series_id)

    return render(request, 'video/video_detail.html', {'video': v_container,
                                                        'final_player_string': pjs_b64_encrypt(final_player_string),
                                                        'translators': translators,
                                                        'editors': editors})


def get_file_jino(request):
    if "HTTP_REFERER" in request.META:
        host = "jkc-videos.tk"
        name = request.GET.get('name', None)
        if name:
            response = redirect("https://{}/videos/{}".format(host, name))
            return response
    raise Http404


