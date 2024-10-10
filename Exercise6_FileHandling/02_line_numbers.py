from string import punctuation

with open("text.txt") as file:
    text = file.readlines()

output_file = open("output.txt", "w")

for row in range(len(text)):
    letters, marks = 0, 0
    for char in text[row]:
        if char.isalpha():
            letters += 1
        elif char in punctuation:
            marks += 1

    output_file.write(f"Line {row + 1}: {text[row].rstrip()} ({letters})({marks})\n")

output_file.close()
