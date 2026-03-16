import random
import string

words = [
    "apple", "banana", "orange", "grape", "peach", "cherry", "lemon", "melon",
    "table", "chair", "window", "door", "floor", "ceiling", "mirror", "lamp",
    "river", "mountain", "ocean", "forest", "desert", "valley", "island", "lake",
    "tiger", "lion", "elephant", "giraffe", "zebra", "panda", "monkey", "rabbit"
]


def update_game_state(secret_word, guessed_letters, guess, lives):
    new_guessed_letters = guessed_letters + [guess]

    if guess in secret_word:
        new_lives = lives
    else:
        new_lives = lives - 1

    return new_guessed_letters, new_lives


def choose_word(words):
    return random.choice(words)


def create_guessed_word(word):
    return ["_"] * len(word)


def process_guess(secret_word, guessed_word, guess):
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            guessed_word[i] = guess


def is_word_complete(guessed_word):
    return "_" not in guessed_word


def play_game(words):
    secret_word = choose_word(words)
    guessed_word = create_guessed_word(secret_word)

    guessed_letters = []
    lives = 6

    print("Welcome to Hangman!")

    while lives > 0 and not is_word_complete(guessed_word):
        print("\nWord:", " ".join(guessed_word))
        print("Lives left:", lives)
        print("Guessed letters:", guessed_letters)

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)
        process_guess(secret_word, guessed_word, guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Wrong guess.")

    if is_word_complete(guessed_word):
        print("\nWinner winner chicken dinner! You guessed the word: ", secret_word)
    else:
        print("\nShitshow. The word was: ", secret_word)


def autoplay(words):
    secret_word = choose_word(words)
    guessed_word = create_guessed_word(secret_word)

    guessed_letters = []
    lives = 6
    alphabets = list(string.ascii_lowercase)
    while lives > 0 and not is_word_complete(guessed_word):
        remaining_letters = [l for l in alphabets if l not in guessed_letters]
        guess = random.choice(remaining_letters)

        print("\nComputer guesses:", guess)

        guessed_letters, lives = update_game_state(secret_word, guessed_letters, guess, lives)

        process_guess(secret_word, guessed_word, guess)

        print("Word:", " ".join(guessed_word))
        print("Lives left:", lives)

        if guess in secret_word:
            print("Computer guessed correctly!")
        else:
            print("Computer guessed wrong.")

    if is_word_complete(guessed_word):
        print("\nComputer guessed correctly. The word was: ", secret_word)
    else:
        print("\nComputer lost badly. The word was: ", secret_word)


def main():
    play_again = "y"
    while play_again == "y":

        mode = input("\nEnter 'p' to play or 'a' for autoplay: ").lower()

        if mode == "p":
            play_game(words)
        elif mode == "a":
            autoplay(words)
        else:
            print("Invalid choice.")

        play_again = input("\nPlay again? (y/n): ").lower()

    print("Thanks for playing brudda")


main()