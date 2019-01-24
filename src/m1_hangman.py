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
                    '|',
                    '|',
                    '|',
                    '|',
                    '|_______',
                    '|_______|']
        self.current_stage = 0
        self.stage_order = {1: self.add_head, 2: self.add_body_upper, 3: self.add_left_arm, 4: self.add_right_arm,
                            5: self.add_body_lower, 6: self.add_left_leg, 7: self.add_right_leg}
        self.max_guesses = 1
        self.guesses_left = 0

    def set_difficulty(self):
        while True:
            num_guesses = input('Input positive integer number of guesses: ')
            if num_guesses.isdigit() and int(num_guesses) > 0:
                break
            else:
                print('Invalid number, read the prompt and try again.')
        self.max_guesses = num_guesses
        self.guesses_left = num_guesses

    def guesses_to_stage(self):
        return round((self.max_guesses - self.guesses_left) / self.max_guesses * 7)

    def update_stage(self):
        next_stage = self.guesses_to_stage()
        while self.current_stage < next_stage:
            self.current_stage = self.current_stage + 1
            self.stage_order[self.current_stage]()

    def update_display(self):
        for i in range(100):
            print()
        for i in range(len(self.man)):
            print(self.man[i])

    def add_head(self):
        self.man[1] = '|     O'

    def add_left_arm(self):
        self.man[2] = '|    /|'

    def add_right_arm(self):
        self.man[2] = '|    /|\\'

    def add_right_leg(self):
        self.man[4] = '|    / \\'

    def add_left_leg(self):
        self.man[4] = '|    /'

    def add_body_upper(self):
        self.man[2] = '|     |'

    def add_body_lower(self):
        self.man[3] = '|     |'


def main():
    """game = WordDisplay()
    for i in range(10):
        game.update_display()
        game.get_input()"""
    man = Hangman()
    man.update_stage(2)
    man.update_display()
    input()
    man.update_stage(3)
    man.update_display()


main()
