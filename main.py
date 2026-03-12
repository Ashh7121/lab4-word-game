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
word = random.choice(words)
guessed_word = []
for i in range(len(word)):
    guessed_word.append("_")


guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    print("Attempts left:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)
    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("Wrong guess.")
        attempts -= 1


if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame over. The word was:", word)
