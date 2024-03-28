import random

# Color codes for different themes
color_themes = {
    "default": {
        "word": "\033[94m",  # Blue
        "attempts": "\033[91m",  # Red
        "reset": "\033[0m"  # Reset to default
    },
    "green": {
        "word": "\033[92m",  # Green
        "attempts": "\033[93m",  # Yellow
        "reset": "\033[0m"  # Reset to default
    },
    "purple": {
        "word": "\033[95m",  # Purple
        "attempts": "\033[96m",  # Cyan
        "reset": "\033[0m"  # Reset to default
    },
    "red": {
        "word": "\033[91m",  # Red
        "attempts": "\033[93m",  # Yellow
        "reset": "\033[0m"  # Reset to default
    }
}

# Font styles
font_styles = {
    "default": "",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "italic": "\033[3m"
}

def choose_word():
    words = ["python", "hangman", "programming", "computer", "code", "algorithm", "debugging", "syntax"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def get_hint(word, guessed_letters):
    remaining_letters = [letter for letter in word if letter not in guessed_letters]
    return random.choice(remaining_letters)

def draw_hangman(incorrect_guesses):
    stages = [
        '''
           --------
           |      |
           |      
           |     
           |     
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     
           |     
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     /|
           |      |
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / 
          ---
        ''',
        '''
           --------
           |      |
           |      O
           |     /|\\
           |      |
           |     / \\
          ---
        '''
    ]
    print(stages[6 - incorrect_guesses])

def hangman():
    print("Welcome to Hangman!")
    theme_choice = input("Choose a color theme (default/green/purple/red): ").lower()
    if theme_choice not in color_themes:
        theme_choice = "default"  # Set default theme if invalid choice

    font_choice = input("Choose a font style (default/bold/underline/italic): ").lower()
    if font_choice not in font_styles:
        font_choice = "default"  # Set default font if invalid choice
    
    print("Selected theme:", theme_choice)
    print("Selected font:", font_choice)

    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0

    while incorrect_guesses < 6:
        print("\nWord:", font_styles[font_choice], color_themes[theme_choice]["word"], display_word(word, guessed_letters), color_themes["default"]["reset"], font_styles["default"])
        print(color_themes[theme_choice]["attempts"], "Attempts left:", 6 - incorrect_guesses, color_themes["default"]["reset"])
        guess = input("Guess a letter or type 'hint' for a hint: ").lower()

        if guess == "hint":
            hint = get_hint(word, guessed_letters)
            print("Hint: The word contains the letter '{}'".format(hint))
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            draw_hangman(incorrect_guesses)
            print("Incorrect guess!")
        
        if "_" not in display_word(word, guessed_letters):
            print("\nCongratulations! You've guessed the word:", word)
            break

    if incorrect_guesses == 6:
        print("\nSorry, you've run out of attempts. The word was:", word)

hangman()