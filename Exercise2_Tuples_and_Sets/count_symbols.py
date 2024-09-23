text = input()

symbols = {}

for char in text:
    if char not in symbols:
        symbols[char] = 0
    symbols[char] += 1

for key, value in sorted(symbols.items()):
    print(f"{key}: {value} time/s")
