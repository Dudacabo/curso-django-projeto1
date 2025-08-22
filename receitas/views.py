from django.shortcuts import render


def home(request):
    return render(request, 'receitas/pages/home.html',)

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html',)