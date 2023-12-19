def masked_word(word):
    """
    Returns a masked version of the given word, where each character is replaced with an asterisk.

    Args:
        word (str): The word to be masked.

    Returns:
        str: The masked word.
    """
    return "*" * len(word)


def update_masked_word(word: str, unknown: str, guess: str) -> str:
    """
    Updates the masked word by replacing the underscores with the guessed letter.

    Args:
        word (str): The original word.
        unknown (str): The masked word with underscores representing unknown letters.
        guess (str): The guessed letter.

    Returns:
        str: The updated masked word with the guessed letter revealed.
    """
    for i in range(len(word)):
        if word[i] == guess:
            unknown = unknown[:i] + guess + unknown[i + 1 :]
    return unknown
