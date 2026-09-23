# dicts_and_tuples.py

student = {
    "name": "Aditi",
    "age": 24,
    "scores": [82, 91, 76],
}

print(student["name"])
print(student.get("email", "not provided"))

student["email"] = "aditi@example.com"
student["age"] = 25

print(student)

for key, value in student.items():
    print(f"{key}: {value}")

# Tuples: fixed, ordered, immutable groupings
point = (3, 4)

x, y = point

print(f"x={x}, y={y}")

# point[0] = 10  # would raise TypeError

coordinates = [(0, 0), (3, 4), (-1, 2)]

for px, py in coordinates:
    print(f"Point: ({px}, {py})")
