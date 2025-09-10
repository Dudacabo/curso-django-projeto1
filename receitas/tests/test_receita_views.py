from django.test import TestCase
from django.urls import reverse, resolve
from receitas import views

class ReceitaViewsTest(TestCase):

    def test_receita_home_view_function_is_correct(self):
        view = resolve(reverse('receitas:home'))
        self.assertIs(view.func, views.home)

    def test_receita_category_view_function_is_correct(self):
        view = resolve(reverse('receitas:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_receita_detail_view_function_is_correct(self):
        view = resolve(reverse('receitas:receita', kwargs={'id': 1}))
        self.assertIs(view.func, views.receita)

    def test_receita_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertEqual(response.status_code, 200)

    def test_receita_home_view_loads_correct_template(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertTemplateUsed(response, "receitas/pages/home.html")    

    def test_receita_home_template_shows_no_receitas_found_if_no_receitas(self):
        response = self.client.get(reverse('receitas:home'))
        self.assertIn(
            '<h1> Não tem receitas aqui :/ </h1>',
            response.content.decode('utf-8')
        )