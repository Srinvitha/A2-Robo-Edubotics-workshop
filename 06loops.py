# loops.py

# for loop over a range
for step in range(5):
    print(f"Movement step: {step}")

# for loop over a list
robot_actions = ["walk", "turn", "wave"]

for action in robot_actions:
    print(f"Executing: {action}")

# while loop with a counter
startup_countdown = 3

while startup_countdown > 0:
    print(f"Robot starting in {startup_countdown}...")
    startup_countdown -= 1

print("BonicBot ready!")

# break and continue
for step in range(10):
    if step == 3:
        continue  # skip this iteration

    if step == 6:
        break  # stop the loop entirely

    print("Step =", step)
