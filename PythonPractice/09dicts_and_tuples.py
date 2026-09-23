# dicts_and_tuples.py

robot = {
    "name": "BonicBot",
    "battery": 82,
    "steps": [10, 90, 1],
}

print(robot["name"])
print(robot.get("mode", "not provided"))

robot["mode"] = "Autonomous"
robot["battery"] = 85

print(robot)

for key, value in robot.items():
    print(f"{key}: {value}")

# Tuples: fixed, ordered, immutable groupings
position = (3, 4)

x, y = position

print(f"Robot position: x={x}, y={y}")

# position[0] = 10  # would raise TypeError

positions = [(0, 0), (3, 4), (-1, 2)]

for px, py in positions:
    print(f"Robot position: ({px}, {py})")
