# guess the number (with difficulty!)
import random


total_guesses = 0


def main():
    print("Welcome!")
    consent()


def consent():
    consent_input = input("Play 'Guess the Number'? Y/N: ").strip().upper()

    if consent_input == "Y":
        choose_difficulty()
    elif consent_input == "N":
        print("Play the game or I will skin alive those you hold dear and douse their wounds in citrus lemon.")
        # for legal reasons that's a joke, i do not and never will indulge in such activies
        consent()
    else:
        print(f"I said Y/N, not Y/{consent_input}.")
        consent()


def choose_difficulty():
    print("Choose your difficulty level.")
    difficulty = input("1 - Easy (1-10), 2 - Medium (1-100), 3 - Hard (1-1000): ").strip()

    if difficulty not in {"1", "2", "3"}:
        print("Please enter 1, 2, or 3.")
        choose_difficulty()
        return

    start_game(difficulty)


def start_game(difficulty):
    global total_guesses

    max_num = 0
    match difficulty:
        case "1":
            max_num = 10
        case "2":
            max_num = 100
        case "3":
            max_num = 1000

    target = random.randint(1, max_num)
    #print(f"--debug: target is {target}")
    total_guesses = 0

    print(f"I'm thinking of a number between 1-{max_num}.")

    while True:
        guess_input = input("Your guess: ").strip()

        if not guess_input.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess_input)

        print("Your guess is: ", guess)
        total_guesses += 1

        if guess == target:
            print(f"Your guess is correct! It was {target}!")
            victory(target)
            break
        elif guess < target:
            print("Go higher!")
        elif guess > target:
            print("Go lower!")


def victory(target):
    print(f"You win! The number was {target}!")
    print(f"You got it in {total_guesses} guesses.")
    consent()


main()
