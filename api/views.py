import requests
from django.http import HttpResponse, JsonResponse, Http404 ,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

from JKSite.settings import SOCIAL_NETWORKS_APPLICATION_IDS, SOCIAL_NETWORKS_APPLICATION_PASSWORDS
from .models import LoginRequest
from .serializers import LoginRequestSerializer
from .encryption import encrypt_byte_string, decrypt_to_byte_string, compare_s


@csrf_exempt
def new_login_request(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if not ('key' in data and data['key'] == 'JediKnightApiLogin'):
            raise Http404()
        # if there are any earlier requests from this ip, they should be deleted
        LoginRequest.objects.filter(ip=data["ip"]).delete()
        serializer = LoginRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    else:
        raise Http404()


@csrf_exempt
def login_request_detail(request, pk):
    key = request.GET.get('key', None)
    if key != 'JediKnightApiLogin':
        raise Http404()
    try:
        login_request = LoginRequest.objects.get(pk=pk)
    except LoginRequest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LoginRequestSerializer(login_request)
        return JsonResponse(serializer.data)
    elif request.method == 'DELETE':
        login_request.delete()
        return HttpResponse(status=204)


def login_externally(request):
    request_id = request.GET.get("request_id", None)
    if not request_id:
        return HttpResponse(status=400)
    try:
        login_request = LoginRequest.objects.get(pk=request_id)
    except LoginRequest.DoesNotExist:
        return HttpResponse(status=400)

    data = encrypt_byte_string(JSONRenderer().render({"login_request_id": login_request.id}))
    if login_request.social_network == "vk":
        url_redirect = "https://oauth.vk.com/authorize?client_id={}&display=page" \
        "&redirect_uri=https://oauth.vk.com/blank.html&response_type=code" \
        "&v=5.85&state={}".format(SOCIAL_NETWORKS_APPLICATION_IDS['vk'], str(data))
    elif login_request.social_network == "yandex":
        url_redirect = "https://oauth.yandex.ru/authorize" \
                       "?response_type=code&client_id={}" \
                       "&state={}".format(SOCIAL_NETWORKS_APPLICATION_IDS['yandex'], data)
    else:
        return HttpResponse(status=400)
    login_request.stage = 2
    login_request.save()
    return HttpResponseRedirect(url_redirect)


def complete_login_process(request):
    access_code = request.GET.get("code", None)
    state = request.GET.get("state", None)
    if not state:
        return HttpResponse(status=400)
    decrypted_state = decrypt_to_byte_string(state)
    stream = BytesIO(decrypted_state)
    data = JSONParser().parse(stream)
    login_request_id = data["login_request_id"]
    if not (access_code and login_request_id):
        return HttpResponse(status=400)

    try:
        login_request = LoginRequest.objects.get(pk=login_request_id)
    except LoginRequest.DoesNotExist:
        raise Http404()

    if login_request.social_network == "vk":
        return HttpResponse(status=400)
    elif login_request.social_network == "yandex":
        request_to_social_network = requests.post("https://oauth.yandex.ru/token",
            data={'grant_type': 'authorization_code',
                  'code': access_code,
                  'client_id': SOCIAL_NETWORKS_APPLICATION_IDS['yandex'],
                  'client_secret': SOCIAL_NETWORKS_APPLICATION_PASSWORDS['yandex'],
                  })
        print(request_to_social_network.content)
    return HttpResponse(status=200)


