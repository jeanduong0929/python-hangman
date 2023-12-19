def get_hangman(life):
    if life == 6:
        hangman = """
        _______
        |     |
              |
              |
              |
              |
      ________|
      """

        return hangman
    elif life == 5:
        hangman = """
      _______
      |     |
      O     |
            |
            |
            |
    ________|
    """
        return hangman
    elif life == 4:
        hangman = """
      _______
      |     |
      O     |
      |     |
            |
            |
    ________|
    """
        return hangman
    elif life == 3:
        hangman = """
      _______
      |     |
      O     |
     /|     |
            |
            |
    ________|
    """
        return hangman
    elif life == 2:
        hangman = """
      _______
      |     |
      O     |
     /|\\    |
            |
            |
    ________|
    """
        return hangman
    elif life == 1:
        hangman = """
      _______
      |     |
      O     |
     /|\\    |
     /      |
            |
    ________|
    """
        return hangman
    elif life == 0:
        hangman = """
      _______
      |     |
      O     |
     /|\\    |
     / \\    |
            |
    ________|
    """
        return hangman
