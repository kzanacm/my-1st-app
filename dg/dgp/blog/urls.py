from django.urls import path
from . import views


urlpatterns = [
    path('', views.postagem_lista, name='hpostagem_lista'),
    path('postagem_detalhe/<int:pk>/', views.postagem_detalhe, name='hpostagem_detalhe'),
]
