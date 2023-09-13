import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = self._load_data()

    def _load_data(self):
        dishes = set()
        temporary = {}

        with open(self.source_path) as file:
            reader = csv.reader(file)
            for row in reader:
                name = row["dish"]
                price = float(row["price"])
                ingredientName = row["ingredient"]
                amount = int(row["recipe_amount"])

                ingredient = Ingredient(ingredientName)

                if name not in temporary:
                    temporary[name] = Dish(name, price)
                temporary[name].add_ingredient_dependency(Ingredient(ingredient), amount)
                temporary[name].add_ingredient_dependency(ingredient, amount)

        return dishes
