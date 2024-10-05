def cookbook(*args):
    recipe_book = {}
    result = []
    for arg in args:
        recipe_name, cuisine, ingredients = arg
        recipe_book[cuisine] = recipe_book.get(cuisine, {})
        recipe_book[cuisine].update({recipe_name: ingredients})

    for cuisine in sorted(recipe_book, key=lambda x: (-len(recipe_book[x]), x)):
        result.append(f"{cuisine} cuisine contains {len(recipe_book[cuisine])} recipes:")

        for recipe in sorted(recipe_book[cuisine]):
            result.append(f"  * {recipe} -> Ingredients: {', '.join(recipe_book[cuisine][recipe])}")

    return "\n".join(result)



# print(cookbook(
#     ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
#     ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
#     ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
#     ("Croissant", "French", ["flour", "butter", "yeast"]),
#     ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"])
# ))

print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
    ))
