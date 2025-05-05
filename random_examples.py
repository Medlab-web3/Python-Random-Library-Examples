import random

# 1. Generate a random integer between 1 and 10 (inclusive)
num = random.randint(1, 10)
print("Random integer between 1 and 10:", num)

# 2. Choose a random item from a list
colors = ['red', 'blue', 'green', 'yellow']
chosen_color = random.choice(colors)
print("Randomly chosen color:", chosen_color)

# 3. Shuffle the elements in the list randomly
random.shuffle(colors)
print("Shuffled list:", colors)

# 4. Take a random sample of 2 items from the list (no repetition)
sampled = random.sample(colors, 2)
print("Random sample of 2 colors:", sampled)

# 5. Generate a random float between 0 and 1
decimal = random.random()
print("Random float between 0 and 1:", decimal)

# 6. Generate a random float between two values
float_range = random.uniform(10.5, 20.5)
print("Random float between 10.5 and 20.5:", float_range)

# 7. Generate a number from a Gaussian distribution (normal distribution)
gauss_num = random.gauss(mu=0, sigma=1)
print("Random number from normal distribution (mean=0, std=1):", gauss_num)
