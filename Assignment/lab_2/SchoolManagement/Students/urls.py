from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name="index"),
    path('',views.home,name="home"),
    path('show/',views.list_students,name="show"),
    path('edit/',views.edit_students,name="edit"),
    path('delete/',views.del_students,name="delete"),
]
