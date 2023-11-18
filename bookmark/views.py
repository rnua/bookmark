from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

# Create your views here.

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']     # fields 빼먹으면 ImproperlyConfigured 에러가 뜬다
    success_url = reverse_lazy('list')
    template_name_suffix = '_create' #원래는 _form이지만 _create로 바꿔줌

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')