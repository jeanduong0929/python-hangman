import os
import random
from typing import List


def get_random_word(file_path) -> List[str]:
    """
    Retrieves a random word from a file.

    Args:
        file_path (str): The path to the file containing the words.

    Returns:
        List[str]: A list containing a randomly chosen word from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found")

    with open(file_path, newline="") as file:
        words = file.read().splitlines()
        return random.choices(words)
