from django.urls import path
from . import views

urlpatterns = [
    path('external-login/', views.login_externally, name='login_externally'),
    path('external-login/new/', views.new_login_request, name='new_login_request'),
    path('external-login/<int:pk>/', views.login_request_detail, name='login_request_detail'),
    path('external-login/complete/', views.complete_login_process, name='login_request_detail'),
]