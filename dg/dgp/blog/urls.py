from django.urls import path
from . import views


urlpatterns = [
    path('', views.postagem_lista, name='hpostagem_lista'),
]
