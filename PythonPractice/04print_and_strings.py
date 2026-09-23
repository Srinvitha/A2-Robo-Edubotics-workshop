# print_and_strings.py

robot_name = "BonicBot"
task_score = 96.4

# Basic print
print("Result ready.")

# Multiple values, custom separator and end
print("a", "b", "c", sep=" - ", end="!\n")

# f-strings (the modern, recommended approach)
print(f"{robot_name} completed the task with a score of {task_score:.1f}%")

# .format() method (common in older codebases)
print("{} completed the task with a score of {:.1f}%".format(robot_name, task_score))

# %-style formatting (legacy, still seen in older Python code)
print("%s completed the task with a score of %.1f%%" % (robot_name, task_score))

# String operations
greeting = "Hello" + ", " + robot_name + "!"

print(greeting.upper())
print(greeting.lower())
print(len(greeting))
