from collections import deque

textiles = deque(map(int, input().split()))
medicines = list(map(int, input().split()))

healing_items = {
    100: "MedKit",
    40: "Bandage",
    30: "Patch"
}

crafted_items = {}

while textiles and medicines:
    textile = textiles.popleft()
    medicine = medicines.pop()
    crafted_value = textile + medicine

    if crafted_value > 100:
        if healing_items[100] not in crafted_items:
            crafted_items[healing_items[100]] = 0
        crafted_items[healing_items[100]] += 1
        medicines[-1] += crafted_value - 100
    elif crafted_value in healing_items:
        if healing_items[crafted_value] not in crafted_items:
            crafted_items[healing_items[crafted_value]] = 0
        crafted_items[healing_items[crafted_value]] += 1
    else:
        medicines.append(medicine + 10)


if not textiles and not medicines:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
else:
    print("Medicaments are empty.")

if crafted_items:
    [print(f"{item} - {count}") for item, count in sorted(crafted_items.items(), key=lambda kvp: (-kvp[1], kvp[0]))]

if medicines:
    medicines.reverse()
    print("Medicaments left: " + ", ". join(map(str, medicines)))

if textiles:
    print("Textiles left: " + ", ".join(map(str, textiles)))
