import random

def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number

def get_guess_from_user(difficulty):
    while True:
        selected_number = input(f"Enter a number between 1 to {difficulty}: ")
        if 1 <= int(selected_number) <= int(difficulty):
            return selected_number
        else:
            print("You need to select a number between 1 -", difficulty)

def compare_results(difficulty, attempts):
    secret_number = generate_number(difficulty)

    for attempt in range(attempts):
        user_guess = get_guess_from_user(difficulty)

        if int(user_guess) == secret_number:
            print("Congratulations! You guessed the correct number.")
            return True
        else:
            print("Incorrect. Try again.")

    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
    return False

def play(difficulty):
    return compare_results(difficulty, 2)

# Example usage:
if __name__ == "__main__":
    difficulty_level = input("Enter the difficulty level (maximum number in the range): ")
    play(difficulty_level)

