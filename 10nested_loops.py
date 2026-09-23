# nested_loops.py

# movement steps
for direction in range(1, 4):
    for step in range(1, 4):
        print(f"Direction {direction}, Step {step}")

print("---")

# environment grid: find coordinates containing an obstacle
grid = [
    [0, 1, 0],
    [1, 0, 1],
    [0, 1, 0],
]

threshold = 0

for row_index, row in enumerate(grid):
    for col_index, value in enumerate(row):
        if value > threshold:
            print(
                f"({row_index},{col_index}) = "
                "Obstacle detected"
            )
