# nested_loops.py

# multiplication table (3x3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")

print("---")

# grid search: find coordinates where a value exceeds a threshold
grid = [
    [3, 8, 2],
    [7, 1, 9],
    [4, 6, 5],
]

threshold = 6

for row_index, row in enumerate(grid):
    for col_index, value in enumerate(row):
        if value > threshold:
            print(
                f"({row_index},{col_index}) = "
                f"{value} exceeds threshold"
            )
