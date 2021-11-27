from random import choice
from drawer import Drawer

class Game():
    words = []
    word = ''
    attempts = 0
    word_letters = []
    used_letters = []
    mistake_letters = []
    guessed_letters = []

    def start_game(self):
        self.word = choice(self.words)
        self.attempts = 6
        self.word_letters = list(self.word)
        self.used_letters = []
        self.mistake_letters = []
        self.guessed_letters = ['_' for _ in range(len(self.word_letters))]
        self.do_game()

    def do_game(self):
        list_of_letters = list(self.word_letters)
        while self.word_letters and self.attempts > 0:
            self.show_game()
            letter = input('Enter the letter ')
            print ('')  # make indent
            if(letter in self.used_letters):
                print('This letter is already used')
            else:
                self.used_letters.append(letter)
                if(letter in self.word_letters and len(letter) == 1):
                    for i in self.word_letters:
                        if(i == letter):
                            self.guessed_letters[list_of_letters.index(i)] = i
                            self.word_letters.remove(i)
                elif letter == 'quit':
                    print('Exiting')
                    return
                elif letter == self.word:
                    self.word_letters.clear()   # all letter guessed
                    break
                else:
                    self.attempts -= 1
                    self.mistake_letters.append(letter)
                if not self.word_letters or self.attempts == 0:
                    self.show_game()

        if not self.word_letters:
            print('You win!')
        elif self.attempts == 0:
            print('You lose!')
            print(f'The word is "{self.word}"')
        self.end_game()

    def end_game(self):
        is_continue = input('Try again? (y/n): ')
        if is_continue == 'y':
            self.start_game()

    def get_words(self):
        with open('data\\words.txt', 'r') as f:
            for i in f.readlines():
                self.words.append(i[:len(i)-1])  # every word must end with '\n' 

    def show_game(self, ):
        print(f'Word: {" ".join(self.guessed_letters)}')
        Drawer.draw_hangman(self.attempts)
        print(f'Mistakes: {", ".join(self.mistake_letters)}')
        print(f'Attemps remain: {self.attempts}')
        print('')   # make indent

    def __init__(self):
        self.get_words()
        self.start_game()

if __name__ == '__main__':
    game = Game()