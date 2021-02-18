from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    #path('create', views.create, name="create"),
    path('addingorder', views.addingorder, name="addingorder"),
    path('photozones', views.photozones, name="photozones"),
    path('price', views.price, name ="price"),
    path('homeroom', views.homeroom, name ="homeroom"),
    path('loftroom', views.loftroom, name ="loftroom"),
    path('smileroom', views.smileroom, name ="smileroom"),
    path('elleroom', views.elleroom, name ="elleroom"),
    path('inroom', views.inroom, name ="inroom"),
    path('freeroom', views.freeroom, name ="freeroom"),
]
