from django.urls import path, re_path
from django.contrib import admin
from . import views





urlpatterns = [
    path('', views.index, name='index'),
    # re_path(r'^\s/(?P<id>\d+)$', views.index, name='index'),
    # re_path(r'^product_details/(?P<id>\d+)$', views.product_details(), name='index'),
    path('', views.ProductListView.as_view(), name='index'),
    path('index-1', views.index1, name='index1'),
    path('index-2', views.index2, name='index2'),
    path('index-3', views.index3, name='index3'),
    path('index-4', views.index4, name='index4'),
    path('index-5', views.index5, name='index5'),
]
# добавили связку. Если кто-то обратьится в каталог.урл преобразование.
