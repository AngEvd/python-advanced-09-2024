def shopping_cart(*args):
    result = ""
    products = {"Soup": [], "Pizza": [], "Dessert": []}
    limits = {"Soup": 3, "Pizza": 4, "Dessert": 2}

    for arg in args:
        if arg == "Stop":
            break
        meal, product = arg
        if product not in products[meal] and len(products[meal]) < limits[meal]:
            products[meal].append(product)

    sorted_products = dict(sorted(products.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    if all(isinstance(value, list) and not value for value in sorted_products.values()):
        result = "No products in the cart!"
    else:
        for meal, products_list in sorted_products.items():
            result += f"{meal}:\n"
            for product in sorted(products_list):
                result += f" - {product}\n"

    return result
