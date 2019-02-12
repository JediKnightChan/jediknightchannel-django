from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from django.template import RequestContext

from news.models import Post
from .forms import FeedbackForm
from .additional import check_recaptcha, save_feedback


def index_page(request):
    latest_posts = Post.objects.filter(date__lte=timezone.now()).order_by('-date')[:2]
    return render(request, 'main/index.html', {'posts': latest_posts})


def swtor_rusifikator(request):
    return render(request, 'main/swtor-rusifikator.html', {})


@check_recaptcha
def contact_page(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid() and request.recaptcha_is_valid:
            save_feedback(form)
            return redirect('index_page')
        else:
            return redirect('contact_page')
    else:
        form = FeedbackForm()

    return render(request, 'main/contact.html', {'form': form})



def handler404(request, *args, **kwargs):
    response = render(request, 'main/404.html', {})
    response.status_code = 403
    return response


def handler403(request, *args, **kwargs):
    response = render(request, 'main/404.html', {})
    response.status_code = 403
    return response