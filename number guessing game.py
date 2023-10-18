import random

def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Congratulations! You guessed the number correctly. It was", secret_number)
            break

        attempts += 1
        print("Attempts left:", max_attempts - attempts)

    if attempts == max_attempts:
        print("You have run out of attempts. The number was", secret_number)

if __name__ == '__main__':
    play_game()
