from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index_page, name='index_page'),
    path('contact/', views.contact_page, name='contact_page'),
    re_path('^swtor-rusifikator/?$', views.swtor_rusifikator, name='swtor_rusifikator'),
    path('404/', views.handler404)
]