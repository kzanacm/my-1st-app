from django.shortcuts import render


def postagem_lista(request):
    return render(request, 'blog/postagem_lista.html', {})
