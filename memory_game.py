
import random
import time
import os

def generate_sequence(difficulty):
    # Generate a sequence of random numbers based on the given difficulty
    numbers = [random.randint(1, 101) for _ in range(int(difficulty))]

    # Display the generated sequence briefly, then clear the screen
    print(' '.join(map(str, numbers)), end='')
    time.sleep(2)
    print('\r ')
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen based on the operating system

    return numbers

def get_list_from_user(difficulty):
    # Get a list of numbers from the user based on the given difficulty
    numbers = []
    words = {0: 'first', 1: 'second', 2: 'third', 3: 'fourth', 4: 'fifth'}

    for i in range(int(difficulty)):
        numbers.append(int(input(f"Enter the {words[i]} number you saw and press Enter: ")))

    return numbers

def is_list_equal(generated_list, player_list):
    # Check if the user's input list is equal to the generated list
    return sorted(generated_list) == sorted(player_list)

def play(difficulty):
    # Allow the user three attempts to guess the sequence
    for attempt in range(3):
        print(f"Attempt {attempt + 1} of 3:")
        generated_list = generate_sequence(difficulty)
        player_list = get_list_from_user(difficulty)

        if is_list_equal(generated_list, player_list):
            print("Congratulations! You remembered the sequence.")
            return True

        print("Incorrect. Try again.")

    print("Sorry, you've run out of attempts. The correct sequence was:", generated_list)
    return False

