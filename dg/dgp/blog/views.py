from django.shortcuts import render
from django.utils import timezone
from .models import Postagem


def postagem_lista(request):
    Postagens = Postagem.objects.filter(ptg_ts_criacao__lte=timezone.now()).order_by('ptg_ts_criacao') 
    return render(request, 'blog/postagem_lista.html', {'Postagens': Postagens})
