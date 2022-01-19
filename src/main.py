from random import choice

class Drawer():
    def draw_hangman(attempts: int) -> None:
        with open(f'data\\pictures\\{attempts}.txt', 'r') as f:
            strings = f.readlines()
            for i in strings:
                print(i, end='')
        print('')   # make indent

class Player():
    def player_input() -> str:
        letter = input('Enter the letter ')
        print ('')  # make indent
        return letter

class Game():
    def __init__(self) -> None:
        self.words = []
        self.get_words()
        self.start()
    
    def start(self) -> None:
        self.word = choice(self.words)
        self.attempts = 6
        self.word_letters = list(self.word)
        self.used_letters = []
        self.mistake_letters = []
        self.guessed_letters = ['_' for _ in range(len(self.word_letters))]
        self.list_of_letters = list(self.word_letters)
        self.loop()

    def loop(self) -> None:
        while self.word_letters and self.attempts > 0:
            self.show_game()
            letter = Player.player_input()
            if(letter in self.used_letters):
                print('This letter is already used')
            else:
                self.used_letters.append(letter)
                if(letter in self.word_letters and len(letter) == 1):
                    for i in self.word_letters:
                        if(i == letter):
                            self.guessed_letters[self.list_of_letters.index(i)] = i
                            self.word_letters.remove(i)
                elif letter == 'quit':
                    print('Exiting')
                    break
                elif letter == self.word:
                    self.word_letters.clear()   # all letters guessed
                    break
                elif not letter == self.word and len(letter) > 1:
                    self.attempts = 0   # if you wrtie word and do not guess
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
        else:
            return
        self.end()

    def end(self) -> None:
        is_continue = input('Try again? (y/n): ')
        if is_continue == 'y':
            self.start()

    def get_words(self) -> None:
        with open('data\\words.txt', 'r') as f:
            for i in f.readlines():
                self.words.append(i[:len(i)-1])  # every word must end with '\n' 

    def show_game(self) -> None:
        print(f'Word: {" ".join(self.guessed_letters)}')
        Drawer.draw_hangman(self.attempts)
        print(f'Mistakes: {", ".join(self.mistake_letters)}')
        print(f'Attemps remain: {self.attempts}')
        print('')   # make indent

if __name__ == '__main__':
    Game()