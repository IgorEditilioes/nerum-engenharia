from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Projeto
from .forms import OrcamentoForm
from .emails import enviar_emails_orcamento


from django.core.mail import send_mail
from .forms import OrcamentoForm
from django.contrib import messages
from django.shortcuts import redirect, render

def index(request):
    projetos = Projeto.objects.all()

    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            orcamento = form.save()

            # Dados do orçamento
            nome = orcamento.nome
            email_cliente = orcamento.email
            telefone = orcamento.telefone
            mensagem = orcamento.mensagem

            # Chama função em outro arquivo
            enviar_emails_orcamento(nome, email_cliente, telefone, mensagem)

            messages.success(request, "Orçamento enviado com sucesso!")
            return redirect('index')

    else:
        form = OrcamentoForm()

    return render(request, 'portfolio/index.html', {
        'form': form,
        'projetos': projetos,
    })



def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projeto_detail.html', {'projeto': projeto})


def solicitar_orcamento(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sua solicitação de orçamento foi enviada com sucesso! Retornaremos em breve.")
            return redirect('solicitar_orcamento')
    else:
        form = OrcamentoForm()

    return render(request, 'contato.html', {'form': form})
