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

print(safe_divide(85, 2))
print(safe_divide(85, 0))

# Catching a specific exception type across a loop
sensor_readings = ["12", "abc", "7"]

for value in sensor_readings:
    try:
        number = int(value)
        print(f"Converted: {number}")

    except ValueError:
        print(f"'{value}' is not a valid number.")
