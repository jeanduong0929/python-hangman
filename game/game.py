import os
from typing import List

from word_generator import get_random_word
from display import get_hangman
from util import masked_word, update_masked_word


def __clear_screen() -> None:
    """
    Clears the terminal screen.

    This function checks the operating system and uses the appropriate command
    to clear the screen. On Windows, it uses the "cls" command, and on Unix-like
    systems, it uses the "clear" command.
    """
    os.system("cls" if os.name == "nt" else "clear")


def __message(msg: str) -> None:
    """
    Display a message on the screen.

    Args:
        msg (str): The message to display.

    Returns:
        None
    """
    __clear_screen()
    print(msg)
    input("\nPress enter to continue...")


def __display(life: int, unknown: str, guesses: List[str]) -> None:
    """
    Display the hangman game interface.

    Args:
        life (int): The remaining life of the player.
        unknown (str): The word to guess, with hidden letters represented by underscores.
        guesses (List[str]): The list of letters guessed by the player.

    Returns:
        None
    """
    hangman = get_hangman(life)
    __clear_screen()
    print("Welcome to Hangman!")
    print(hangman)
    print(f"Life: {life}")
    print(f"Guesses: {', '.join(guesses)}")
    print(f"Word to guess: {unknown}")


def start(life: int, random_word: str) -> None:
    """
    Starts the hangman game.

    Args:
        life (int): The number of lives the player has.
        random_word (str): The word to be guessed.

    Returns:
        None
    """
    guesses = []
    unknown = masked_word(random_word)

    while life > 0:
        __display(life, unknown, guesses)

        guess = input("\nGuess a letter: ")

        if guess == "":
            __message("Please enter a letter!")
            continue

        if guess in guesses:
            __message("You already guessed that letter!")
            continue
        else:
            guesses.append(guess)

        if guess not in random_word:
            life -= 1
            __message("Incorrect!")
            continue

        unknown = update_masked_word(random_word, unknown, guess)
        __message("Correct!")

        if unknown == random_word:
            break

    if life > 0:
        __message(f"You win! The word was {random_word}.")
    else:
        __message(f"You lose! The word was {random_word}.")


if __name__ == "__main__":
    file_path = "resources/words.txt"
    random_word = get_random_word(file_path)[0]
    start(6, random_word)
