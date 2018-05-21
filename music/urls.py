from django.urls import path,re_path
from . import views

app_name = 'music'
urlpatterns = [
    path('',views.IndexView.as_view(), name='index'),
    #/music/songs/
    path('songs/',views.SongsList.as_view(), name='songs'),
    #/music/12/
    re_path(r'^(?P<pk>[0-9]+)/',views.DetailView.as_view(), name = 'detail'),
    #/music/album/add
    path('album/add/',views.AlbumCreate.as_view(),name='album_add'),
    #/music/album/2/delete
    re_path('album/(?P<pk>[0-9]+)/delete/',views.AlbumDelete.as_view(),name='album_delete'),
    #/music/album/2
    re_path('album/(?P<pk>[0-9]+)/',views.AlbumUpdate.as_view(),name='album_update'),
]
''''
#/music/
    path('',views.index, name='index'),
    #/music/12/
    re_path(r'^(?P<album_id>[0-9]+)/',views.detail, name = 'detail'),
#/music/12/favorite/
    re_path(r'^(?P<album_id>[0-9]+)/favorite/',views.favorite, name = 'favorite'),
'''
