from .test_receita_base import ReceitaTestBase, Receita
from django.core.exceptions import ValidationError
from parameterized import parameterized


class ReceitaModelTest(ReceitaTestBase):
    def setUp(self) -> None:
        self.receita = self.make_receita()
        return super().setUp()
    
    def make_receita_no_defaults(self):
        receita = Receita(
        category=self.make_category(name='Test Default Category'),
        author=self.make_author(username='newuser'),
        title='Receita Title',
        description='Receita Description',
        slug='receita-slug',
        preparation_time=10,
        preparation_time_unit='Minutos',
        servings=5,
        servings_unit='Porções',
        preparation_steps='Receita Preparation Steps',
        )
        receita.full_clean()
        receita.save()
        return receita
    

    @parameterized.expand([
            ("title", 65),
            ("description", 165),
            ("preparation_time_unit", 65),
            ("servings_unit", 65),
        ])
    def test_receita_fields_mx_lengh(self, field, max_length):
        setattr(self.receita, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.receita.full_clean()


    def test_receita_preparation_steps_is_html_is_false_by_default(self):
        receita = self.make_receita_no_defaults()            
        self.assertFalse(receita.preparation_steps_is_html, msg='Receita preparation_steps_is_html não é falso',)

    def test_receita_is_published_is_false_by_default(self):
        receita = self.make_receita_no_defaults()            
        self.assertFalse(receita.is_published, msg='Receita is_published não é falso',)

    def test_receita_string_representation(self):
        needed = 'Testing Representation'
        self.receita.title = needed
        self.receita.full_clean()
        self.receita.save()
        self.assertEqual(str(self.receita), needed, msg=f'A representação da string de receitas deve ser'f'"{needed}" mas "{str(self.receita)}" que foi recebio.')



