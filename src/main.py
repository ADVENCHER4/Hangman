from random import choice
from drawer import Drawer

class Game():
    words = []

    def get_words(self):
        with open('data\\words.txt', 'r') as f:
            for i in f.readlines():
                self.words.append(i[:len(i)-1])  # every word must end with '\n' 
    def start_game(self):
        word = choice(self.words)
        chars = set(word)
        attempts = 6
        used_letters = []
        Drawer.draw_hangman(6)
        while chars and attempts > 0:
            letter = input('Enter letter ')
            if(letter in used_letters):
                print('This letter is already used')
            else:
                used_letters.append(letter)
                if(letter in chars and len(letter) == 1):
                    chars.remove(letter)
                    print('Correct!\n')
                elif letter == 'quit':
                    print('Exiting')
                    break
                else:
                    print('Not correct!\n')
                    attempts -= 1
                    print(f'Attemps remain {attempts}')
                Drawer.draw_hangman(attempts)
        if not chars:
            print('You win!')
        elif attempts == 0:
            print('You lose!')
        else:
            return
        print(f'Word is {word}')
        is_continue = input('Try again? (y/n): ')
        if is_continue == 'y':
            self.start_game()
    def __init__(self):
        self.get_words()
        self.start_game()

if __name__ == '__main__':
    game = Game()