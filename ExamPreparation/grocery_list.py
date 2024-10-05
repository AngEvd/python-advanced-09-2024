def shop_from_grocery_list(budget: int, grocery: list,  *args: tuple[str, float]) -> str:
    shopping_cart = []
    for item, price in args:
        if item in grocery and item not in shopping_cart:
            if price <= budget:
                shopping_cart.append(item)
                budget -= price
            else:
                break

    missing_products = [item for item in grocery if item not in shopping_cart]

    if missing_products:
        return f"You did not buy all the products. Missing products: {', '.join(missing_products)}."
    else:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
