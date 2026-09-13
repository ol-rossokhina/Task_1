from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from tests.constants import BUN_NAME, BUN_PRICE, FILLING_NAME, FILLING_PRICE, SAUCE_NAME, SAUCE_PRICE


@pytest.fixture
def mock_bun():
    # Мок булочки: изолируем Burger от реальной реализации Bun.
    bun = Mock()
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def mock_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = SAUCE_NAME
    ingredient.get_price.return_value = SAUCE_PRICE
    return ingredient


@pytest.fixture
def mock_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = FILLING_NAME
    ingredient.get_price.return_value = FILLING_PRICE
    return ingredient


@pytest.fixture
def burger():
    return Burger()
