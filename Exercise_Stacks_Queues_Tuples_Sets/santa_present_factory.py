from collections import deque

materials = list(map(int, input().split()))
magic_levels = deque(map(int, input().split()))

presents_map = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

presents = {}

while materials and magic_levels:
    material = materials.pop()
    magic_level = magic_levels.popleft()

    if material == 0 and magic_level == 0:
        continue
    elif material == 0:
        magic_levels.appendleft(magic_level)
        continue
    elif magic_level == 0:
        materials.append(material)
        continue

    total_magic_level = material * magic_level

    if total_magic_level in presents_map:
        present_name = presents_map[total_magic_level]
        if present_name not in presents:
            presents[present_name] = 0
        presents[present_name] += 1
    elif total_magic_level < 0:
        materials.append(material + magic_level)
    elif total_magic_level > 0:
        materials.append(material + 15)

if ("Wooden train" in presents and "Doll" in presents) or ("Teddy bear" in presents and "Bicycle" in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(map(str, reversed(materials)))}")

if magic_levels:
    print(f"Magic left: {', '.join(map(str, magic_levels))}")

for name, qty in sorted(presents.items()):
    print(f"{name}: {qty}")
