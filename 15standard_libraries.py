import random
from datetime import datetime

# random
dice_roll = random.randint(1, 6)
print(f"Dice roll: {dice_roll}")

colors = ["red", "green", "blue", "yellow"]

chosen_color = random.choice(colors)
print(f"Chosen color: {chosen_color}")

shuffled = colors.copy()
random.shuffle(shuffled)

print(f"Shuffled: {shuffled}")

# datetime
now = datetime.now()

print(f"Current time: {now}")
print(f"Formatted: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Day of week: {now.strftime('%A')}")
