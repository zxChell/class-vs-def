from django.urls import path
from posts.views import *

urlpatterns = [
    path('list/', ListViewClass.as_view(), name='list'),
    path('create/', CreateViewClass.as_view(), name='create'),
]
