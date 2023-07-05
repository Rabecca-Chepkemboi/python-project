import pygame
pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

hangman_stages = [
    """
       +---+
           |
           |
           |
           |
       ========
    """,
    """
       +---+
       O   |
           |
           |
           |
       ========
    """,
    """
       +---+
       O   |
       |   |
           |
           |
       ========
    """,
    """
       +---+
       O   |
      /|   |
           |
           |
       ========
    """,
    """
       +---+
       O   |
      /|\  |
           |
           |
       ========
    """,
    """
       +---+
       O   |
      /|\  |
      /    |
           |
       ========
    """,
    """
       +---+
       O   |
      /|\  |
      / \  |
           |
       ========
    """
]

def play_hagman():
    word = "hagman"
    guessed_letters = []
    tries = 6

    while tries > 0:
        masked_word = ""
        for letter in word:
            if letter in guessed_letters:
                masked_word += letter + ""
            else:
                masked_word += "_"

        print("Guess the word:", masked_word)    
        guess = input("Entre a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print  (hangman_stages[6 - tries])

            if tries == 0:
                print("sorry you lost. The word was", word)
                break

            else:
                if all(letter in guessed_letters for letter in word):
                    print("Congratulations, you won!")
                    break
    print("Thanks for playing hagman")       
    play_hagman()     


pygame.display.update()

