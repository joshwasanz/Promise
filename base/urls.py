from django.urls import path
from . import views


urlpatterns = [

    path("login/",views.loginPage,name='login'),

    path("",view=views.home,name="home"),
    path("room/<str:pk>/",view=views.room,name="room"),
    path("create-room/",view=views.createRoom,name="create-room"),
    path("update-room/<str:pk>/",view=views.updateRoom,name="update-room"),
    path("delete-room/<str:pk>/",view=views.deleteRoom,name="delete-room")
]