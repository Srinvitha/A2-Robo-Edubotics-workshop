# conditionals.py

score = 82

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} -> Grade: {grade}")

# Comparison and logical operators
temperature_c = 5
is_raining = True

if temperature_c < 10 and is_raining:
    print("Wear a warm, waterproof jacket.")
elif temperature_c < 10:
    print("Wear a warm jacket.")
elif is_raining:
    print("Bring an umbrella.")
else:
    print("No jacket needed.")
