# lists_and_strings.py

students = ["Aditi", "Rahul", "Meera"]
scores = [82, 91, 76]

print(students[0], scores[0])  # indexing
print(students[-1])            # negative indexing
print(students[0:2])           # slicing

students.append("Kabir")
scores.append(88)

print(students, scores)
print("Number of students:", len(students))

# pairing list data with zip + a for loop
for name, score in zip(students, scores):
    print(f"{name}: {score}")

# basic string manipulation
report_line = "Aditi,82,Pass"

parts = report_line.split(",")

print(parts)

name, score_text, status = parts

summary = f"{name.upper()} scored {score_text} — {status}"

print(summary)

names_joined = ", ".join(students)

print("Class roster:", names_joined)
