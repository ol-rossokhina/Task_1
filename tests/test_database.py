from unittest.mock import patch

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:
    """Тесты класса Database."""

    def test_available_buns_returns_three_buns(self):
        database = Database()

        buns = database.available_buns()

        assert len(buns) == 3

    def test_available_ingredients_returns_six_ingredients(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    def test_available_ingredients_contains_sauces_and_fillings(self):
        database = Database()

        types = {ingredient.get_type() for ingredient in database.available_ingredients()}

        assert types == {INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING}

    @patch('praktikum.database.Bun')
    def test_init_creates_buns_via_bun_class(self, mock_bun):
        # Мокаем класс Bun, чтобы проверить, что Database создаёт булки
        # именно через конструктор Bun с нужными аргументами,
        # не проверяя реальную реализацию класса Bun.
        Database()

        assert mock_bun.call_count == 3
        mock_bun.assert_any_call('black bun', 100)
        mock_bun.assert_any_call('white bun', 200)
        mock_bun.assert_any_call('red bun', 300)

    @patch('praktikum.database.Ingredient')
    def test_init_creates_ingredients_via_ingredient_class(self, mock_ingredient):
        # Мокаем класс Ingredient, чтобы убедиться, что Database
        # формирует список из 6 ингредиентов через вызовы конструктора.
        Database()

        assert mock_ingredient.call_count == 6
        mock_ingredient.assert_any_call(INGREDIENT_TYPE_SAUCE, 'hot sauce', 100)
        mock_ingredient.assert_any_call(INGREDIENT_TYPE_FILLING, 'cutlet', 100)
