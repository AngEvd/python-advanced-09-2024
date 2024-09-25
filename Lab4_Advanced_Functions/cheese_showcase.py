def sorting_cheeses(**kwargs):
    result = ""
    cheeses_dict = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))
    for cheese_name, quantity in cheeses_dict:
        result += f"{cheese_name}\n"
        sorted_quantity = sorted(quantity, reverse=True)
        result += "\n".join(str(el) for el in sorted_quantity) + "\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
