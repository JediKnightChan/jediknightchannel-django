from django.urls import path
from . import views

urlpatterns = [
    path('', views.base_categories_list, name='base_categories_list'),
    path('<int:pk>', views.category_detail, name='category_detail'),
    path('watch/<int:pk>', views.video_detail, name='video_detail'),
    path('get-file/', views.get_file_jino, name="get_video_jino"),
]
