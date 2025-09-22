from .test_receita_base import ReceitaTestBase
from django.core.exceptions import ValidationError


class ReceitaModelTest(ReceitaTestBase):
    def setUp(self) -> None:
        self.receita = self.make_receita()
        return super().setUp()

    def test_receita_title_raises_error_if_title_has_more_than_65_chars(self):
        self.receita.title = "A" * 70

        with self.assertRaises(ValidationError):
            self.receita.full_clean()
            
