from django.urls import path
from . import views

urlpatterns = [
    path('', views.dialogue_list, name='dialogue_list'),
    path('dialogue/<int:pk>', views.dialogue_detail, name='dialogue_detail'),
    path('handler/', views.message_handler, name='message_detail'),
    path('npc/', views.npc_search, name='npc_search'),
    path('common_handler/', views.common_handler, name="common_handler"),
]