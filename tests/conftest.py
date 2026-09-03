from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    # Мок булочки: изолируем Burger от реальной реализации Bun.
    bun = Mock()
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = 'hot sauce'
    ingredient.get_price.return_value = 50.0
    return ingredient


@pytest.fixture
def mock_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = 'cutlet'
    ingredient.get_price.return_value = 150.0
    return ingredient


@pytest.fixture
def burger():
    return Burger()
