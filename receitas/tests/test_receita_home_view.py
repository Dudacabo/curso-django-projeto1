from django.urls import reverse, resolve
from receitas import views
from .test_receita_base import ReceitaTestBase
from unittest.mock import patch

class ReceitaHomeViewTest(ReceitaTestBase):
                
    def test_receita_home_view_function_is_correct(self):
        view = resolve(reverse('receitas:home'))
        self.assertIs(view.func, views.home)

    def test_receita_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertEqual(response.status_code, 200)

    def test_receita_home_view_loads_correct_template(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertTemplateUsed(response, "receitas/pages/home.html")    

    def test_receita_home_template_shows_no_receitas_found_if_no_receita(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertIn(
            '<h1> Não tem receitas aqui :/ </h1>',
            response.content.decode('utf-8')
        )

    def test_receita_home_template_loads_receitas(self):
        # Cria uma receita
        self.make_receita()

        response = self.client.get(reverse('receitas:home'))
        content = response.content.decode('utf-8')
        response_context_receitas = response.context['receitas']

        # Checa se uma receita existe
        self.assertIn('Receita Title', content)
        self.assertEqual(len(response_context_receitas), 1)

    def test_receita_home_template_dont_load_receitas_not_published(self):
        """Testa receita is_published False não aparece """

        # Cria uma receita
        self.make_receita(is_published=False)

        response = self.client.get(reverse('receitas:home'))

        # Checa se uma receita existe
        self.assertIn(
            '<h1> Não tem receitas aqui :/ </h1>',
            response.content.decode('utf-8')
        ) 

    def test_receita_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_receita(**kwargs)

        with patch('receitas.views.PER_PAGE', new=3):
            response = self.client.get(reverse('receitas:home'))
            receitas = response.context['receitas']
            paginator = receitas.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)