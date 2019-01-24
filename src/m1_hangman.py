"""
Hangman.

Author: Zach Kelly.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.
import random


class WordDisplay(object):
    def __init__(self):
        self.solution = ''
        self.displayed = ''
        self.choose_word()
        self.hide_word()
        self.not_guessed = []
        for i in range(97, 123):
            self.not_guessed.append(chr(i))
        self.guess_amount = 3

    def hide_word(self):
        self.displayed = len(self.solution) * '*'

    def show_letter(self, a):
        letter_present = 0
        new = ''
        for i in range(len(self.solution)):
            if self.displayed[i] == '*' and self.solution[i] == a:
                new = new + a
                letter_present = 1
            else:
                new = new + self.displayed[i]
        self.displayed = new
        if letter_present == 0:
            self.guess_amount = self.guess_amount - 1

    def get_input(self):
        while True:
            guess = input('Input a single character guess: ')
            guess.lower()
            if guess.isalpha() and len(guess) == 1:
                if self.not_guessed.count(guess) == 0:
                    print('You\'ve already guessed that letter!')
                else:
                    break
            else:
                print('Invalid guess, read the prompt and try again.')
        self.not_guessed.remove(guess)
        self.show_letter(guess)

    def choose_word(self):
        with open('words.txt') as words:
            words.readline()
            word_list = words.read().split()
        index = random.randrange(0, len(word_list))
        self.solution = word_list[index]

    def update_display(self):
        for i in range(100):
            print()
        print(self.displayed)


class Hangman(object):
    def __init__(self):
        self.man = ['_______',
                    '|     O',
                    '|    /|\\',
                    '|     |',
                    '|    / \\',
                    '|_______',
                    '|_______|']

    def update_display(self):
        for i in range(len(self.man)):
            print(self.man[i])

    def remove_left_arm(self):
        self.man[2] = '|     |\\'

    def remove_right_arm(self):
        self.man[2] = '|     |'

    def remove_left_leg(self):
        self.man[4] = '|      \\'

    def remove_left_leg(self):
        self.man[4] = '|'

    def remove_body_lower(self):
        self.man[3] = '|'

    def remove_body_lower(self):
        self.man[2] = '|'


def main():
    """game = WordDisplay()
    for i in range(10):
        game.update_display()
        game.get_input()"""
    man = Hangman()
    man.update_display()


main()