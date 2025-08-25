from django.shortcuts import render
from utils.receitas.factory import make_receita

def home(request):
    return render(request, 'receitas/pages/home.html', context={
        'receitas': [make_receita() for _ in range(10)],
    })

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': make_receita(),
    })