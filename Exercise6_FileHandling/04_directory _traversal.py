import os

files = {}
directory = input("Enter a directory: ")
directory = os.path.abspath(directory)


def get_files_ext(folder, level=1):
    if level == 0:
        return
    for element in os.listdir(folder):
        f = os.path.join(directory, element)
        if os.path.isfile(f):
            extension = os.path.splitext(element)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(element)
        else:
            get_files_ext(f, level - 1)


try:
    get_files_ext(directory)
except FileNotFoundError:
    print("Directory not found")

with open(os.path.join(directory, "report.txt"), "w") as file:
    for ext, file_names in sorted(files.items()):
        file.write(f"{ext}\n")
        for file_name in sorted(file_names):
            file.write(f"- - - {file_name}\n")
