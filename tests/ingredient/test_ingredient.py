from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ingredient01 = Ingredient("pepino")
    ingredient02 = Ingredient("farinha")
    ingredient03 = Ingredient("carne")
    ingredient04 = Ingredient("carne")

    assert ingredient01.name == "pepino"
    assert ingredient02.name == "farinha"
    assert ingredient03.name == "carne"
    assert ingredient04.name == "carne"
    assert ingredient02.restrictions == {
        Restriction.GLUTEN,
    }
    assert ingredient03.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }


    assert ingredient01.__eq__(ingredient02) is False
    assert ingredient03.__eq__(ingredient04) is True

    assert repr(ingredient01) == "Ingredient('pepino')"
    assert repr(ingredient02) == "Ingredient('farinha')"

    assert hash(ingredient01) != hash(ingredient02)
    assert hash(ingredient03) == hash(ingredient04)
