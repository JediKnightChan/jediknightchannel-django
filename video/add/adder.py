import requests
from django.utils import timezone
from os.path import join as path_join
from lxml import html
from bs4 import BeautifulSoup
from video.models import VideoContainer, VideoCategory, VideoFile

root_dir = "E:/films/Star Wars/cw1/text/"
filename = path_join(root_dir, "list.html")
wiki_url = "https://ru.wikipedia.org/wiki/Список_эпизодов_мультсериала_«Войны_клонов»_2008_года"


def download_page(url):
    r = requests.get(url)
    with open(filename, 'wb') as output_file:
        output_file.write(r.content)


def get_morals():
    rus_morals = []
    tree = html.parse(filename)
    els = tree.xpath('//td[@colspan="5"]')
    for el in els:
        if el.text and "Девиз серии" in el.text:
            rus_morals.append(el.text.replace("Девиз серии: ", "").strip())
    return rus_morals


def get_titles(bgcolor):
    rus_titles = []
    with open(filename, 'rb') as file:
        soup = BeautifulSoup(file, features="lxml")
        tr_list = soup.find_all('tr', {'bgcolor': bgcolor})
        for tr in tr_list:
            td = tr.find_all('td')[1]
            title_str = td.text
            en, rus = title_str.split(" / ")
            rus_titles.append(rus.strip())
    return rus_titles


def get_titles_and_morals(beg, end):
    titles = get_titles('#F2F2F2')[beg:end]
    morals = get_morals()[beg:end]
    if len(titles) != len(morals):
        raise ValueError("Different lens")
    return titles, morals


if __name__ == '__main__':
    name_template = "{0}-я серия: {1}"
    image_template = "sw_clone_wars/cw1/img/{}.png"
    video_url_template = "sw_clone_wars/cw1/{0}/{1}.mp4"
    season1 = VideoCategory.objects.get(pk=3)
    beg = 0
    end = 22
    titles, morals = get_titles_and_morals(beg, end)
    for counter, tm_tuple in enumerate(zip(titles, morals)):
        vc_title, vc_moral = tm_tuple
        vc_name = name_template.format(counter+1, vc_title)
        vc_image_url = image_template.format(counter+1)
        vc_time = timezone.now()
        vc = VideoContainer.objects.create(name=vc_name, date=vc_time,
                                      short_description=vc_moral, image_url_ending=vc_image_url)
        vc.save()
        vc.categories.add(season1)

        en_url = video_url_template.format("en", counter+1)
        vf_en = VideoFile(parent_video_container=vc, video_as_track_name="English", url_ending=en_url)
        vf_en.save()

        ru_url = video_url_template.format("ru", counter+1)
        vf_ru = VideoFile(parent_video_container=vc, video_as_track_name="Русский", url_ending=ru_url)
        vf_ru.save()
        break


