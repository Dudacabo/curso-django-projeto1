from django.test import TestCase
from receitas.models import Category, Receita, User

class ReceitaTestBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        receita = Receita.objects.create(
            category=category,
            author=author,
            title = 'Receita Title',
            description = 'Receita Description' ,
            slug = 'receita-slug',
            preparation_time = 10,
            preparation_time_unit = "Minutos" ,
            servings = 5,
            servings_unit = "Porções",
            preparation_steps = "Receita Preparation Steps",
            preparation_steps_is_html = False,
            is_published = True,
        )
        return super().setUp()