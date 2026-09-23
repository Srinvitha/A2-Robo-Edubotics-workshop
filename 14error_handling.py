# error_handling.py

def safe_divide(a, b):
    try:
        result = a / b

    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

    else:
        print("Division succeeded.")
        return result

    finally:
        print("Division attempt finished.")

print(safe_divide(10, 2))
print(safe_divide(10, 0))

# Catching a specific exception type across a loop
values = ["12", "abc", "7"]

for value in values:
    try:
        number = int(value)
        print(f"Converted: {number}")

    except ValueError:
        print(f"'{value}' is not a valid number.")
