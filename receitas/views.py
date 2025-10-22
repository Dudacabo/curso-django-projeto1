from django.shortcuts import render, get_list_or_404, get_object_or_404
from receitas.models import Receita
from django.http.response import Http404
from django.db.models import Q


def home(request):
    receitas = Receita.objects.filter(is_published = True,).order_by('-id')

    return render(request, 'receitas/pages/home.html', context={
        'receitas': receitas,
    })


def category(request, category_id):
    receitas = get_list_or_404( 
        Receita.objects.filter(
        category__id=category_id, is_published = True, ).order_by('-id')
    )
    
    return render(request, 'receitas/pages/category.html', context={
        'receitas': receitas,
        'title': f'{receitas[0].category.name} - Category | '
    })


def receita(request, id):
    receita = get_object_or_404(Receita, id=id, is_published = True, )
    
    return render(request, 'receitas/pages/receita-view.html', context={
        'receita': receita,
        'is_detail_page' : True
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()
    
    receitas = Receita.objects.filter(Q(title__icontains=search_term) | Q(description__icontains=search_term),).order_by('-id')
    
    return render(request, "receitas/pages/search.html", {'page_title': f'Pesquisa por "{search_term}" |', 'search_term': search_term, "receitas": receitas })