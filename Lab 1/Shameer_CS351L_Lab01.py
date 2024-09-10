import random

# Non-AI Version: Player vs Computer
def non_ai_version():
    number = random.randint(1, 100)
    guess = None
    attempts = 0
    
    while guess != number:
        guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1
        
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

# AI Version: Binary Search (Computer vs Player)
def binary_search_version(number):
    low = 1
    high = 100
    attempts = 0
    
    while low <= high:
        mid = (low + high) // 2
        print(f"AI guesses: {mid}")
        attempts += 1
        
        if mid < number:
            low = mid + 1
        elif mid > number:
            high = mid - 1
        else:
            print(f"AI guessed the number {mid} in {attempts} attempts.")
            break

# BFS Version
def bfs_version(number):
    queue = list(range(1, 101))
    attempts = 0
    
    while queue:
        guess = queue.pop(0)
        attempts += 1
        print(f"AI guesses: {guess}")
        
        if guess == number:
            print(f"AI guessed the number {guess} in {attempts} attempts.")
            break

# DFS Version
def dfs_version(number):
    stack = list(range(1, 101))
    attempts = 0
    
    while stack:
        guess = stack.pop()
        attempts += 1
        print(f"AI guesses: {guess}")
        
        if guess == number:
            print(f"AI guessed the number {guess} in {attempts} attempts.")
            break

# Custom Algorithm (Simulated Annealing)
def simulated_annealing_version(number):
    current_guess = random.randint(1, 100)
    attempts = 0
    temperature = 100
    
    while temperature > 0:
        print(f"AI guesses: {current_guess}")
        attempts += 1
        if current_guess == number:
            print(f"AI guessed the number {current_guess} in {attempts} attempts.")
            break
        
        temperature -= 1
        next_guess = current_guess + random.choice([-1, 1]) * random.randint(1, temperature)
        if next_guess > 0 and next_guess <= 100:
            current_guess = next_guess

# Running the non-AI version (uncomment to run)
# non_ai_version()

# Running AI versions with a fixed number (you can change this number for testing)
number_to_guess = 57
binary_search_version(number_to_guess)
bfs_version(number_to_guess)
dfs_version(number_to_guess)
simulated_annealing_version(number_to_guess)
