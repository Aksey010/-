import random


class Loto:
    def __init__(self):
        self.card = ''
        self.current_number = None
        self.numbers_in_game = list(range(1, 91))
        self.card_number = None
        self.player_name = ''
        self.bot = None

    def __str__(self):
        return 'Made by Aksey_010'

    def __eq__(self, other):
        return self.card_number == other.card_number

    def refill_numbers_in_game(self):
        self.numbers_in_game = list(range(1, 91))

    def get_random_number(self):
        self.current_number = random.sample(self.numbers_in_game, 1)
        self.numbers_in_game.remove(self.current_number[0])

    def new_card_number(self):
        self.card_number = random.sample(range(1, 91), 15)

    def compute_card(self):

        a = self.card_number[:5]
        b = self.card_number[5:10]
        c = self.card_number[10:15]

        for i in range(len(a)):
            if a[i] < 10:
                a[i] = str(a[i])
                a[i] = a[i] + ' '

        for i in range(len(b)):
            if b[i] < 10:
                b[i] = str(b[i])
                b[i] = b[i] + ' '

        for i in range(len(c)):
            if c[i] < 10:
                c[i] = str(c[i])
                c[i] = c[i] + ' '

        _ = random.sample(range(0, 6), 3)
        for i in _:
            a.insert(i, '  ')

        _ = random.sample(range(0, 6), 3)
        for i in _:
            b.insert(i, '  ')

        _ = random.sample(range(0, 6), 3)
        for i in _:
            c.insert(i, '  ')

        a = ' ' + str(a).replace(',', '').replace("'", "").replace('[', '').replace(']', '')
        b = ' ' + str(b).replace(',', '').replace("'", "").replace('[', '').replace(']', '')
        c = ' ' + str(c).replace(',', '').replace("'", "").replace('[', '').replace(']', '')

        d = a + '\n' + b + '\n' + c

        self.card = d

    def show_card(self, name=''):
        print(name.center(25, '-'))
        print(self.card)
        print(25*'-')

    def pass_in_card(self):
        if self.current_number[0] > 9:
            self.card = self.card.replace(' ' + str(self.current_number[0]), ' --')
        else:
            self.card = self.card.replace(' ' + str(self.current_number[0]) + ' ', ' --')
