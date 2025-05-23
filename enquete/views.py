from django.http import HttpResponse
from django.shortcuts import render

from enquete.models import Questao

def index(request):
    questoes = Questao.objects.order_by('descricao')
    contexto = {'questoes': questoes}
    return render(request, 'enquete/index.html', contexto)



