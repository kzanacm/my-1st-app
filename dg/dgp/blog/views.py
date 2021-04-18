from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Postagem


def postagem_lista(request):
    postagens = Postagem.objects.filter(ptg_ts_criacao__lte=timezone.now()).order_by('ptg_ts_criacao') 
    return render(request, 'blog/postagem_lista.html', {'postagens': postagens})


def postagem_detalhe(request, pk):
    postagem = get_object_or_404(Postagem, pk=pk)
    return render(request, 'blog/postagem_detalhe.html', {'postagem': postagem})
