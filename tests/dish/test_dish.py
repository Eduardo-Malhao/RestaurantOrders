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

    big.add_ingredient_dependency(tomate, 1)
    big.add_ingredient_dependency(carne, 2)
    mc.add_ingredient_dependency(carne, 1)
    mc.add_ingredient_dependency(pepino, 2)

    assert mc.get_restrictions() == {
        Restriction.ANIMAL_DERIVED,
        Restriction.ANIMAL_MEAT,
    }

    assert mc.get_ingredients() == {
        Ingredient("carne"),
        Ingredient("pepino"),
    }
    assert mc.recipe == {Ingredient("carne"): 1, Ingredient("pepino"): 2}

    with pytest.raises(ValueError) as error:
        Dish("pepino", -1000)
    assert str(error.value) == "Dish price must be greater then zero."

    with pytest.raises(TypeError) as error:
        Dish("carne", "1000")
    assert str(error.value) == "Dish price must be float."
