
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Album


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class SongsList(generic.ListView):
    template_name = 'music/songs.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']



class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','genre','album_logo']




























"""
from django.shortcuts import render, get_object_or_404
#from django.http import Http404
# Create your views here.
#from django.http import HttpResponse
from .models import Album, Songs
#from django.template import loader

'''
def index(request):
    all_album = Album.objects.all()
    template = loader.get_template("music\index.html")
    context = {
    'all_albums': all_album,

    }
    return HttpResponse(template.render(context, request))
'''

def index(request):
    all_album = Album.objects.all()
    content ={'all_albums':all_album}
    return render(request,'music/index.html',content)
    
def detail(request,album_id):
    '''
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    '''
    album = get_object_or_404(Album, pk=album_id)
    return render(request,'music/detail.html',{'album':album})

def favorite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.songs_set.get(pk=request.POST['song'])
    except (KeyError,Songs.DoesNotExist):
        return render(request,'music/detail.html' , {
            'album':album,
            'error_message':"You did not select a valid song",
            })
    else:
        selected_song.is_favorite = True
        selected_song.save()
        return render(request,'music/detail.html',{'album':album})
"""    
        
