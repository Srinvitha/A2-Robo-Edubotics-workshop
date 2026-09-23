import random
from datetime import datetime

# random movement
movement_steps = random.randint(1, 6)
print(f"Random movement steps: {movement_steps}")

directions = ["forward", "backward", "left", "right"]

chosen_direction = random.choice(directions)
print(f"Chosen direction: {chosen_direction}")

shuffled = directions.copy()
random.shuffle(shuffled)

print(f"Random direction sequence: {shuffled}")

# datetime
now = datetime.now()

print(f"Current time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Day of week: {now.strftime('%A')}")
