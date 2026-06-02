
def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        if letter not in guesses:
            guesses.append(letter)
        clue = ""
        for i in secret_word:
            if i in guesses:
                clue = clue + i
            else:
                clue = clue + '_'
        print(clue)
        if '_' in clue:
            return False
        else:
            return True
    return hangman_closure

hangman_secret = input('What is the secret word?: ')
game = make_hangman(hangman_secret)
guess = False

while guess == False:
    guess = game(input("Guess a letter: "))
