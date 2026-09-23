# loops.py

# for loop over a range
for i in range(5):
    print(f"Count: {i}")

# for loop over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")

# while loop with a counter
countdown = 3

while countdown > 0:
    print(f"Launching in {countdown}...")
    countdown -= 1

print("Liftoff!")

# break and continue
for n in range(10):
    if n == 3:
        continue  # skip this iteration

    if n == 6:
        break  # stop the loop entirely

    print("n =", n)
