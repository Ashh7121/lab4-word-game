import random
words = [
    "apple", "banana", "orange", "grape", "peach", "cherry", "lemon", "melon",
    "table", "chair", "window", "door", "floor", "ceiling", "mirror", "lamp",
    "river", "mountain", "ocean", "forest", "desert", "valley", "island", "lake",
    "tiger", "lion", "elephant", "giraffe", "zebra", "panda", "monkey", "rabbit",
    "pencil", "paper", "notebook", "marker", "eraser", "ruler", "folder", "scissors",
    "music", "guitar", "piano", "drums", "violin", "trumpet", "flute", "singer",
    "rocket", "planet", "galaxy", "comet", "asteroid", "satellite", "spaceship", "orbit",
    "bread", "butter", "cheese", "pizza", "pasta", "salad", "soup", "sandwich",
    "happy", "brave", "calm", "eager", "fancy", "gentle", "jolly", "kind",
    "travel", "journey", "adventure", "explore", "discover", "wander", "voyage", "roam"
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
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nGame over. The word was:", secret_word)


def main():
    words = ["python", "coding", "hangman", "computer"]

    play_again = "y"
    while play_again == "y":
        play_game(words)
        play_again = input("\nPlay again? (y/n): ").lower()

    print("Thanks for playing!")


main()