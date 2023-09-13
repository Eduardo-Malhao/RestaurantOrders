from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    mc = Dish("MC Lanche", 18.00)
    big = Dish("Big Mac", 12.99)

    assert mc.name == "MC Lanche"
    assert mc.price == 18.00

    assert repr(mc) == "Dish('MC Lanche', R$18.00)"
    assert repr(big) == "Dish('Big Mac', R$12.99)"

    assert hash(mc) == hash("Dish('MC Lanche', R$18.00)")
    assert hash(big) != hash("xernous")

    assert mc.__eq__(mc) is True
    assert big.__eq__(mc) is False

    tomato = Ingredient("tomato")
    hamburguer = Ingredient("hamburguer")
    cheese = Ingredient("cheese")

    big.add_ingredient_dependency(tomato, 1)
    big.add_ingredient_dependency(hamburguer, 2)
    mc.add_ingredient_dependency(hamburguer, 1)
    mc.add_ingredient_dependency(cheese, 2)

    assert mc.recipe == {tomato: 1, hamburguer: 1, cheese: 2}

    assert mc.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert mc.get_ingredients() == {tomato, hamburguer, cheese}

    with pytest.raises(TypeError):
        Dish("Invalid Dish", "invalid_price")

    with pytest.raises(ValueError):
        Dish("Invalid Dish", -10.0)

    assert mc.recipe.get(tomato) == 1
    assert mc.recipe.get(hamburguer) == 1
    assert mc.recipe.get(cheese) == 2

    xernous = Ingredient("xernous")
    assert mc.recipe.get(xernous) is None