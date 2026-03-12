from main import update_game_state


def test_correct_guess():
    secret_word = "python"
    guessed_letters = ["p", "y"]
    guess = "t"
    lives = 6

    new_letters, new_lives = update_game_state(secret_word, guessed_letters, guess, lives)

    assert new_letters == ["p", "y", "t"]
    assert new_lives == 6
    print("test_correct_guess passed")


def test_wrong_guess():
    secret_word = "python"
    guessed_letters = ["p", "y"]
    guess = "z"
    lives = 6

    new_letters, new_lives = update_game_state(secret_word, guessed_letters, guess, lives)

    assert new_letters == ["p", "y", "z"]
    assert new_lives == 5
    print("test_wrong_guess passed")


def test_immutability():
    secret_word = "python"
    guessed_letters = ["p", "y"]
    guess = "t"
    lives = 6

    new_letters, new_lives = update_game_state(secret_word, guessed_letters, guess, lives)

    assert guessed_letters == ["p", "y"]  # original list unchanged
    print("test_immutability passed")


if __name__ == "__main__":
    test_correct_guess()
    test_wrong_guess()
    test_immutability()