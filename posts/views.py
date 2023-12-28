from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
# Create your views here.


class ListViewClass(ListView):
    model = Post
    fields = '__all__'


# class DetailViewClass(DetailView):
#     model = Post
#
#
class CreateViewClass(CreateView):
    model = Post
    fields = '__all__'
    success_url = '/list'

#
#
# class UpdateViewClass(UpdateView):
#     model = Post
#     fields = '__all__'
#
#
# class DeleteViewClass(DetailView):
#     model = Post
#