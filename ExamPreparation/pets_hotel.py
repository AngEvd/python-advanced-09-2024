def accommodate_new_pets(capacity: int, limit: float, *args: tuple) -> str:
    hotel = {}
    pets_to_accommodate = len(args)
    for pet in args:
        if capacity == 0:
            break
        if pet[1] <= limit:
            if pet[0] not in hotel:
                hotel[pet[0]] = 0
            hotel[pet[0]] += 1
            capacity -= 1
        pets_to_accommodate -= 1
    if pets_to_accommodate == 0:
        result = f"All pets are accommodated! Available capacity: {capacity}."
    else:
        result = "You did not manage to accommodate all pets!"
    result += "\nAccommodated pets:"
    for key, value in sorted(hotel.items(), key=lambda kvp: kvp[0]):
        result += f"\n{key}: {value}"

    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))
print()
print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
print()

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))




