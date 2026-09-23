# file_basics.py

names = ["Aditi", "Rahul", "Meera"]

with open("students.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

with open("students.txt", "r") as f:
    content = f.read()

print(content)

with open("students.txt", "r") as f:
    for line in f:
        print(f"Student: {line.strip()}")

with open("students.txt", "a") as f:
    f.write("Kabir\n")

with open("students.txt", "r") as f:
    all_lines = f.readlines()

print(all_lines)
