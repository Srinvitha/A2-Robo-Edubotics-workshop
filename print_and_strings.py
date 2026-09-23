# print_and_strings.py

name = "Rahul"
score = 91.5

# Basic print
print("Result ready.")

# Multiple values, custom separator and end
print("a", "b", "c", sep=" - ", end="!\n")

# f-strings (the modern, recommended approach)
print(f"{name} scored {score:.1f}%")

# .format() method (common in older codebases)
print("{} scored {:.1f}%".format(name, score))

# %-style formatting (legacy, still seen in older Python code)
print("%s scored %.1f%%" % (name, score))

# String operations
greeting = "Hello" + ", " + name + "!"

print(greeting.upper())
print(greeting.lower())
print(len(greeting))
