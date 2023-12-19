from word_generator import get_random_word


def start():
    print("Game started")


if __name__ == "__main__":
    file_path = "resources/words.txt"
    random_word = get_random_word(file_path)
