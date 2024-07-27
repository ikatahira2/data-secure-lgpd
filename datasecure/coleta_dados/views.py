from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DadosUsuarioForm

def index(request):
    if request.method == 'POST':
        form = DadosUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Dados recebidos e salvos com sucesso.")
    else:
        form = DadosUsuarioForm()
    return render(request, 'coleta_dados/index.html', {'form': form})
