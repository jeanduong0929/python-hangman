from word_generator import get_random_word
from display import get_hangman


def start(life, random_word):
    hangman = get_hangman(life)
    print(hangman)


if __name__ == "__main__":
    file_path = "resources/words.txt"
    random_word = get_random_word(file_path)
    start(6, random_word)
