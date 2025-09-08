from django.http import Http404
from django.shortcuts import render
from utils.receitas.factory import make_receita
from receitas.models import Receita


def home(request):
    receitas = Receita.objects.filter(is_published = True,).order_by('-id')
    return render(request, 'receitas/pages/home.html', context={
        'receitas': receitas,
    })

def category(request, category_id):
    receitas = Receita.objects.filter(
        category__id=category_id, is_published = True, ).order_by('-id')
    
    if not receitas:
        raise Http404('Not Found ;) ')
    
    return render(request, 'receitas/pages/category.html', context={
        'receitas': receitas,
        'title': f'{receitas.first().category.name} - Category | '
    })

def receita(request, id):
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': make_receita(),
        'is_detail_page' : True
    })