from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, Http404
from main.additional import check_recaptcha

from .models import GameClass, NPCDialogue, CommonGameFile


def dialogue_list(request):
    game_classes = GameClass.objects.order_by('index')
    return render(request, 'translation/dialogue_list.html', {'game_classes': game_classes})


@check_recaptcha
def dialogue_detail(request, pk):
    if request.recaptcha_is_valid:
        print("Valid")
        dialogue = get_object_or_404(NPCDialogue, pk=pk)
        string_pairs = dialogue.get_dialogue_strings_pairs()
        return render(request, 'translation/dialogue_detail.html', {'dialogue' : dialogue, 'string_pairs': string_pairs})
    else:
        return render(request, 'translation/recaptcha.html', {})


def npc_search(request):
    common_file = CommonGameFile.objects.get(name='NPC')
    return render(request, 'translation/npc_search.html', {'common_file': common_file})


def message_handler(request):
    key = request.GET.get('key', None)
    game_file_name = request.GET.get('filename', None)
    index = request.GET.get('index', None)
    message = request.GET.get('message', None)
    if game_file_name and index and message and key == "JKCorrection":
        with open("editing_messages.txt", "a") as file:
            file.write("{}, {}: {}\r\n\r\n".format(game_file_name, index, message))
        return JsonResponse({"success": True})
    else:
        raise Http404()


def common_handler(request):
    if "HTTP_REFERER" in request.META:
        result_html = ""
        key = request.GET.get('key', None)
        game_file_pk = request.GET.get('file', None)
        search_string = request.GET.get('search_string', None)
        if game_file_pk and search_string and key == "JKSearch":
            game_common_file = CommonGameFile.objects.get(pk=game_file_pk)
            string_tuples = game_common_file.get_content_strings_pairs()
            for en_string, ru_string, index in string_tuples:
                found_string = None
                if search_string in en_string:
                    found_string = ru_string
                elif search_string in ru_string:
                    found_string = en_string
                if found_string:
                    result_html += '<li><span class="found">{}</span></li>'.format(found_string)
            if not result_html:
                result_html = '<li>По вашему запросу ничего не найдено</li>'
            return JsonResponse({"result_html": result_html})
    raise Http404()
