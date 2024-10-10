symbols = ("-", ",", ".", "!", "?")

with open("text.txt") as file:
    for row, line in enumerate(file.readlines()):
        if row % 2 == 0:
            for symbol in symbols:
                line = line.replace(symbol, "@")
            print(" ".join(reversed(line.split())))
