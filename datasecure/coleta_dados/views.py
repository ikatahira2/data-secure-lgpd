# coleta_dados/views.py

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        consentimento = request.POST.get('consentimento')
        if consentimento:
            # Aqui você pode salvar os dados no banco de dados ou processá-los conforme necessário
            return HttpResponse(f"Dados recebidos: Nome: {nome}, Email: {email}, Telefone: {telefone}")
    return render(request, 'coleta_dados/index.html')
