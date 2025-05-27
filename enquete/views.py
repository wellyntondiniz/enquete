from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from enquete.models import Questao


def index(request):
    questoes = Questao.objects.order_by('descricao')
    contexto = {'questoes': questoes}
    return render(request, 'enquete/index.html', contexto)

def resultados(request, id_questao):
    question = Questao(pk=id_questao)
    context = {'question': question}
    return render(request, 'enquete/resultados.html', context)

def votar(request, id_questao):
    questao = get_object_or_404(Questao, pk=id_questao)
    try:
        selected_option = questao.alternativa_set.get(pk=request.POST['option'])
    except KeyError:
        return render(request, 'enquete/voto.html', {
            'questao': questao,
            'error_message': "Selecione uma opção",
        })
    else:
        selected_option.votos += 1
        selected_option.save()
        return HttpResponseRedirect(reverse('enquete:resultados', args=(id_questao,)))



