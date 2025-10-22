from django.urls import reverse, resolve
from receitas import views
from .test_receita_base import ReceitaTestBase

class ReceitaSearchViewTest(ReceitaTestBase):

    def test_receita_search_uses_correct_view_function(self):
        resolved = resolve(reverse('receitas:search'))
        self.assertIs(resolved.func, views.search)

    def test_receita_search_loads_correct_template(self):
        response = self.client.get(reverse('receitas:search') + '?q=teste')
        self.assertTemplateUsed(response, "receitas/pages/search.html")

    def test_receita_search_raises_404_if_no_search_term(self):
        url = reverse('receitas:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_receita_search_term_is_on_page_title_and_escaped(self):
        url = reverse('receitas:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn('Pesquisa por &quot;&lt;Teste&gt;&quot;', response.content.decode('utf-8'))


