from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *

@login_required
def home(request):

    context = {}

    return render(request, 'home.html', context)

@login_required
def consorcio_cadastro(request, tipo_venda, tipo_pessoa):

    form = ConsorcioForm()

    print(tipo_venda)
    print(tipo_pessoa)

    if request.method == "POST":
        form = ConsorcioForm(request.POST)
        form.save()

        return redirect('/')

    context = {'form': form}

    return render(request, 'consorcio/cadastro.html', context)

@login_required
def consorcio_relatorio(request):

    tipo_venda = request.GET.get('tipo_venda')

    if tipo_venda is None:
        relatorios = Consorcio.objects.filter(Tipo_Venda='Interna')
    else:
        relatorios = Consorcio.objects.filter(Tipo_Venda=tipo_venda)

    context = {'relatorios': relatorios}

    return render(request, 'consorcio/relatorio.html', context)


@login_required
def administradora_lista(request):

    administradoras = RegraComissionamento.objects.all()

    form = AdministradoraForm()
    formComissionamento = RegraComissionamentoForm()

    if request.method == "POST":
        form = AdministradoraForm(request.POST)
        form.save()

        formComissionamento = RegraComissionamentoForm(request.POST)
        formComissionamento.save()

        ultimo_comissionamento = RegraComissionamento.objects.last()
        ultimo_comissionamento.Administradora = Administradora.objects.last()
        ultimo_comissionamento.save()
        
        return redirect('/')

    context = {'form': form, 'formComissionamento': formComissionamento, 'administradoras': administradoras}

    return render(request, 'administradora/lista.html', context)


@login_required
def representante_lista(request):

    representantes = Representante.objects.all()

    form = RepresentanteForm()

    if request.method == "POST":
        form = RepresentanteForm(request.POST)
        form.save()

        return redirect('/')

    context = {'form': form, 'representantes': representantes}

    return render(request, 'representante/lista.html', context)