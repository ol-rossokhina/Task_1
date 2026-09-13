from unittest.mock import Mock

import pytest

from tests.constants import BUN_NAME, BUN_PRICE, FILLING_NAME, FILLING_PRICE, SAUCE_NAME, SAUCE_PRICE


class TestBurgerSetBuns:
    """Тесты установки булочки бургера."""

    def test_set_buns_sets_bun_attribute(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun is mock_bun


class TestBurgerAddIngredient:
    """Тесты добавления ингредиента в бургер."""

    def test_add_ingredient_appends_to_list(self, burger, mock_sauce):
        burger.add_ingredient(mock_sauce)

        assert burger.ingredients == [mock_sauce]

    def test_add_ingredient_twice_keeps_order(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.ingredients == [mock_sauce, mock_filling]


class TestBurgerRemoveIngredient:
    """Тесты удаления ингредиента из бургера."""

    def test_remove_ingredient_removes_correct_item(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.remove_ingredient(0)

        assert burger.ingredients == [mock_filling]


class TestBurgerMoveIngredient:
    """Тесты перемещения ингредиента внутри бургера."""

    def test_move_ingredient_changes_order(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_filling, mock_sauce]


class TestBurgerGetPrice:
    """Тесты подсчёта цены бургера."""

    def test_get_price_with_no_ingredients_counts_only_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.get_price() == BUN_PRICE * 2

    @pytest.mark.parametrize(
        'ingredient_prices, expected_extra',
        [
            ([SAUCE_PRICE], SAUCE_PRICE),
            ([SAUCE_PRICE, FILLING_PRICE], SAUCE_PRICE + FILLING_PRICE),
            ([], 0.0),
        ],
    )
    def test_get_price_sums_bun_and_ingredients(self, burger, mock_bun, ingredient_prices, expected_extra):
        burger.set_buns(mock_bun)
        for price in ingredient_prices:
            ingredient = Mock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == BUN_PRICE * 2 + expected_extra


class TestBurgerGetReceipt:
    """Тесты формирования чека бургера."""

    def test_get_receipt_contains_bun_name_twice(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        receipt = burger.get_receipt()

        assert receipt.count(BUN_NAME) == 2

    def test_get_receipt_contains_ingredient_lines(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        receipt = burger.get_receipt()

        assert f'sauce {SAUCE_NAME}' in receipt
        assert f'filling {FILLING_NAME}' in receipt

    def test_get_receipt_contains_price(self, burger, mock_bun, mock_sauce):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)

        receipt = burger.get_receipt()

        assert f'Price: {BUN_PRICE * 2 + SAUCE_PRICE}' in receipt
