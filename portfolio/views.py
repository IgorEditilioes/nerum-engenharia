from django.shortcuts import render, get_object_or_404
from .models import Projeto

# Create your views here.
def index(request):
    projetos = Projeto.objects.all()
    return render(request, 'portfolio/index.html', {'projetos':projetos})

def projeto_detail(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'portfolio/projeto_detail.html', {'projeto': projeto})