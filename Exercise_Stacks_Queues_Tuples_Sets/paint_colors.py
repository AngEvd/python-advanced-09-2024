from collections import deque

substrings = deque(input().split())

main_colors = {"red", "yellow", "blue"}
secondary_colors = {"orange", "purple", "green"}

secondary_map = {
    "orange": ("red", "yellow"),
    "purple": ("red", "blue"),
    "green": ("yellow", "blue"),
}

paint = []

while substrings:
    left = substrings.popleft()
    right = substrings.pop() if substrings else ""

    color = left + right
    reverse_color = right + left

    if color in main_colors or color in secondary_colors:
        paint.append(color)
    elif reverse_color in main_colors or reverse_color in secondary_colors:
        paint.append(reverse_color)
    else:
        left = left[:-1]
        right = right[:-1]
        if left:
            substrings.insert(len(substrings) // 2, left)
        if right:
            substrings.insert(len(substrings) // 2, right)

final_colors = []
for color in paint:
    if color in secondary_colors:
        required_colors = secondary_map[color]
        if all(c in paint for c in required_colors):
            final_colors.append(color)
    else:
        final_colors.append(color)

print(final_colors)
