from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html', context={'info': Todo.objects.all()})


def create(request):
    if request.method == 'POST':
        form = AddModelTask(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create.html', context={'form': AddModelTask()})


def update(request, id):
    task = Todo.objects.get(id=id)
    if request.method == 'POST':
        form = AddUpdateModelTask(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'create.html', context={'form': AddUpdateModelTask(instance=task)})


def delete(request, id):
    task = get_object_or_404(Todo, id=id)
    task = Todo.objects.get(id=id)
    task.delete()
    return redirect('index')


class BaseViewClosed(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'info': Todo.objects.filter(status=True)})


class BaseViewCreate(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'create.html', context={'form': AddModelTask()})

    def post(self, request, *args, **kwargs):
            form = AddModelTask(data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('index')
            return self.get(request, *args, **kwargs)


class BaseViewDetail(View):
    def get(self, request, pk, *args, **kwargs):
        try:
            task = get_object_or_404(Todo, pk=pk)
        except:
            return redirect('index')
        return render(request, 'index.html', context={'task': task})


class BaseViewDetailUpdate(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        return render(request, 'create.html', context={'form': AddUpdateModelTask(instance=task)})

    def post(self, request, pk, *args, **kwargs):
            task = Todo.objects.get(pk=pk)
            form = AddUpdateModelTask(data=request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect('index')
            return self.get(request, *args, **kwargs)


class BaseViewDelete(View):
    def get(self, request, pk, *args, **kwargs):
        task = get_object_or_404(Todo, pk=pk)
        task.delete()
        return redirect('index')


class List(ListView):
    model = Todo
    # # template_name = 'index.html'
    # # content_objects_name = 'info'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['text'] = 'Made for Alabuga'
    #     return context
    #
    # def get_queryset(self, **kwargs):
    #     # queryset = super().get_context_data(**kwargs)
    #     queryset = Todo.objects.filter(status=True)
    #     return queryset


class Detail(DetailView):
    model = Todo


class CreateViewClass(CreateView):
    model = Todo
    fields = '__all__'
    success_url = '/list'


class UpdateViewClass(UpdateView):
    model = Todo
    fields = '__all__'
    success_url = '/list'


class DeleteViewClass(DeleteView):
    model = Todo
    success_url = reverse_lazy('list')

