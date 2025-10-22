from django.urls import reverse, resolve
from receitas import views
from .test_receita_base import ReceitaTestBase

class ReceitaCategoryViewTest(ReceitaTestBase):

    def test_receita_category_view_function_is_correct(self):
        view = resolve(reverse('receitas:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    def test_receita_category_view_returns_404_if_no_receitas_found(self):
        response = self.client.get(reverse('receitas:category', kwargs={'category_id': 1000}))
        self.assertEqual(response.status_code, 404)

    def test_receita_category_template_loads_receita(self):
        needed_title = 'This is a category test'
        # Cria uma receita
        self.make_receita(title=needed_title)

        response = self.client.get(reverse('receitas:category', args=(1,)))
        content = response.content.decode('utf-8')

        # Checa se o titulo está no template
        self.assertIn(needed_title, content)

    def test_receita_category_template_dont_load_receitas_not_published(self):
        """Testa receita is_published False não aparece """

        # Cria uma receita
        receita = self.make_receita(is_published=False)

        response = self.client.get(reverse('receitas:receita', kwargs={'id': receita.category.id}))

        self.assertEqual(response.status_code, 404)



