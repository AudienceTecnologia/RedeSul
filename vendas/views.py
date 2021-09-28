from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from .models import *
from .forms import *
from users.models import *
from users.forms import *

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
        
        return redirect('/administradora_lista')

    context = {'form': form, 'formComissionamento': formComissionamento, 'administradoras': administradoras}

    return render(request, 'administradora/lista.html', context)

@login_required
def administradora_edit(request, administradora_id, comissionamento_id):

    administradoras = RegraComissionamento.objects.all()

    administradora = get_object_or_404(Administradora, pk=administradora_id)
    comissionamento = get_object_or_404(RegraComissionamento, pk=comissionamento_id)

    form = AdministradoraForm(instance=administradora)
    formComissionamento = RegraComissionamentoForm(instance=comissionamento)

    if request.method == "POST":
        form = AdministradoraForm(request.POST, instance=administradora)
        form.save()

        formComissionamento = RegraComissionamentoForm(request.POST, instance=comissionamento)
        formComissionamento.save()

        return redirect('/administradora_lista')

    context = {'form': form, 'formComissionamento': formComissionamento, 'administradoras': administradoras}

    return render(request, 'administradora/edit.html', context)

@login_required
def administradora_nova_regra(request, administradora_id, comissionamento_id):

    formNovaRegra = RegraComissionamentoForm()

    if request.method == "POST":

        formNovaRegra = RegraComissionamentoForm(request.POST)
        formNovaRegra.save()

        return redirect('/administradora_lista')

    context = {'formNovaRegra': formNovaRegra}

    return render(request, 'administradora/nova_regra.html', context)

@login_required
def administradora_delete(request, id):

    administradora = get_object_or_404(RegraComissionamento, pk=id)
    administradora.delete()

    return redirect('/administradora_lista')

@login_required
def representante_lista(request):

    representantes = Representante.objects.all()

    form = RepresentanteForm()

    if request.method == "POST":
        form = RepresentanteForm(request.POST)
        form.save()

        return redirect('/representante_lista')

    context = {'form': form, 'representantes': representantes}

    return render(request, 'representante/lista.html', context)

@login_required
def representante_edit(request, id):

    representante = get_object_or_404(Representante, pk=id)

    form = RepresentanteForm(instance=representante)

    if request.method == "POST":
        form = RepresentanteForm(request.POST, instance=representante)
        form.save()

        return redirect('/representante_lista')

    context = {'form': form}

    return render(request, 'representante/edit.html', context)

@login_required
def representante_delete(request, id):

    representante = get_object_or_404(Representante, pk=id)
    representante.delete()

    return redirect('/representante_lista')

@login_required
def financiamento_cadastro(request, tipo_venda, tipo_pessoa):

    form = FinanciamentoForm()

    if request.method == "POST":
        form = FinanciamentoForm(request.POST)
        form.save()

        return redirect('/')

    context = {'form': form}

    return render(request, 'financiamento/cadastro.html', context)

@login_required
def financiamento_relatorio(request):

    relatorios = Financiamento.objects.all()

    context = {'relatorios': relatorios}

    return render(request, 'financiamento/relatorio.html', context)

@login_required
def homeequity_cadastro(request, tipo_venda, tipo_pessoa):

    form = HomeEquityForm()

    if request.method == "POST":
        form = HomeEquityForm(request.POST)
        form.save()

        return redirect('/')

    context = {'form': form}

    return render(request, 'homeequity/cadastro.html', context)

@login_required
def homeequity_relatorio(request):

    relatorios = HomeEquity.objects.all()

    context = {'relatorios': relatorios}

    return render(request, 'homeequity/relatorio.html', context)

@login_required
def user_edit_name(request, id):
    user = get_object_or_404(User, pk=id)
    
    form = UserChangeForm(instance=user)

    if request.method == 'POST':

        form = UserChangeForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
        
        return redirect('/user_lista')

    context = {'form': form}

    return render(request, 'user/edit_name.html', context)

@login_required
def change_password(request):

    form = PasswordChangeForm(request.user)
    
    if request.method == 'POST':
        
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            
            return redirect('/user_lista')

    return render(request, 'user/change_password.html', {'form': form})

@login_required
def user_lista(request):

    users = User.objects.all()

    form = UserCreationForm()
    
    if request.method == 'POST':
        
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            ultimo_user = get_object_or_404(User, pk=User.objects.last().id)

            ultimo_user.Nivel_Acesso = request.POST.get('Nivel_Acesso')
            ultimo_user.CNPJ = request.POST.get('CNPJ')
            ultimo_user.Status = request.POST.get('Status')
            ultimo_user.save()

    context = {'users': users, 'form': form}

    return render(request, 'user/lista.html', context)

@login_required
def user_delete(request, id):

    user = get_object_or_404(User, pk=id)
    user.delete()

    return redirect('/user_lista')

@login_required
def user_edit(request, id):
    user = get_object_or_404(User, pk=id)
    
    form = UserChangeForm(instance=user)

    if request.method == 'POST':

        form = UserChangeForm(request.POST, instance=user)
        
        if form.is_valid():
            form.save()
        
        return redirect('/user_lista')

    context = {'form': form}

    return render(request, 'user/edit.html', context)