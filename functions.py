# functions.py

def convert_c_to_f(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

def describe_temperature(celsius, unit="C"):
    if unit == "F":
        value = convert_c_to_f(celsius)
        label = "F"
    else:
        value = celsius
        label = "C"

    return f"{value:.1f}°{label}"

print(describe_temperature(20))
print(describe_temperature(20, unit="F"))

def greet(name, times=1):
    for _ in range(times):
        print(f"Hello, {name}!")

greet("Priya")
greet("Priya", times=3)
