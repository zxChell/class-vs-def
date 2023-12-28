from django.urls import path
from app.views import *


urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('closed/', BaseViewClosed.as_view(), name='closed'),
    path('create_class/', BaseViewCreate.as_view(), name='create_class'),
    path('detail/<int:pk>', BaseViewDetail.as_view(), name='detail'),
    path('update_class/<int:pk>', BaseViewDetailUpdate.as_view(), name='update_class'),
    path('delete_class/<int:pk>', BaseViewDelete.as_view(), name='delete_class'),
    path('list', List.as_view(), name='list'),
    path('detail_View/<int:pk>', Detail.as_view(), name='detail_view'),
    path('createView/', CreateViewClass.as_view(), name='createView'),
    path('updateView/<int:pk>', UpdateViewClass.as_view(), name='updateView'),
    path('deleteViewClass/<int:pk>', DeleteViewClass.as_view(), name='DeleteView'),

]
