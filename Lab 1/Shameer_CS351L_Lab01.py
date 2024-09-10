import random

def number_guessing_game():
    # The computer selects a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Player has 10 attempts to guess the number

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100. You have 10 attempts.")

    # Loop for the player to make guesses
    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            return

    print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.")

# Run the game
number_guessing_game()
def ai_number_guessing_game():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    low = 1
    high = 100
    attempts = 0

    # Loop until the AI guesses the number correctly
    while low <= high:
        guess = (low + high) // 2  # AI uses binary search to guess
        attempts += 1

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return
        elif feedback == 'h':
            high = guess - 1  # If too high, reduce the upper bound
        elif feedback == 'l':
            low = guess + 1  # If too low, increase the lower bound

    print("Something went wrong!")

# Run the AI version
ai_number_guessing_game()

from collections import deque

def bfs_number_guessing_game():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    number_range = list(range(1, 101))
    queue = deque(number_range)  # BFS uses a queue
    attempts = 0

    # Loop until the AI guesses the number
    while queue:
        guess = queue.popleft()  # BFS takes from the front of the queue
        attempts += 1

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return

    print("Something went wrong!")

# Run the BFS version
bfs_number_guessing_game()



def dfs_number_guessing_game():
    # Player selects a number
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it.")
    number_range = list(range(1, 101))
    stack = number_range[::-1]  # DFS uses a stack (reverse to simulate depth-first search)
    attempts = 0

    # Loop until the AI guesses the number
    while stack:
        guess = stack.pop()  # DFS takes from the end of the list
        attempts += 1

        print(f"AI's guess is: {guess}")
        feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

        if feedback == 'c':
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return

    print("Something went wrong!")

# Run the DFS version
dfs_number_guessing_game()


import random

# Genetic Algorithm for guessing the number
def ga_number_guessing_game():
    print("Think of a number between 1 and 100, and I (the AI) will try to guess it using Genetic Algorithm.")

    # Hyperparameters for the GA
    population_size = 10
    mutation_rate = 0.1
    generations = 20

    # Initialize the population with random guesses between 1 and 100
    population = [random.randint(1, 100) for _ in range(population_size)]
    attempts = 0

    def fitness(guess, feedback):
        """Fitness function based on how close the guess is to the number."""
        return abs(feedback - guess)

    # Loop for multiple generations
    for gen in range(generations):
        attempts += 1
        print(f"Generation {gen+1}")

        # AI guesses the best candidate from the population
        guess = random.choice(population)
        print(f"AI's guess: {guess}")
        feedback = int(input("Enter how close the guess is (1-100) or '0' if correct: "))

        if feedback == 0:
            print(f"I (AI) guessed the number in {attempts} attempts!")
            return

        # Sort population based on fitness (smaller distance to the feedback is better)
        population = sorted(population, key=lambda x: fitness(x, feedback))

        # Select the top 50% of the population (elitism)
        top_half = population[:population_size//2]

        # Generate new guesses through crossover and mutation
        new_population = top_half.copy()

        while len(new_population) < population_size:
            parent1 = random.choice(top_half)
            parent2 = random.choice(top_half)
            child = (parent1 + parent2) // 2  # Simple crossover by averaging two parents
            if random.random() < mutation_rate:
                child += random.randint(-5, 5)  # Apply mutation by slightly altering the child
            new_population.append(min(max(child, 1), 100))  # Ensure the guess is within the range

        population = new_population

    print("AI couldn't guess the number in the allowed generations.")

# Run the Genetic Algorithm version
ga_number_guessing_game()
