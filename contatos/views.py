from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato

# Create your views here. 

def index(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True # Se quiser mostrar os contatos ocultos mudo para False
    )
    paginator = Paginator(contatos, 1)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def olhar_contato(request, contato_id):
    contatos = get_object_or_404(Contato,id=contato_id)

    if not contatos.mostrar:
        raise Http404()

    return render(request, 'contatos/olhar_contato.html', {
        'contato': contatos
    })