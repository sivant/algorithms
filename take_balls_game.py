"""
שני שחקנים משחקים במשחק.
בתחילת המשחק, יש בקופה N גולות.
השחקנים משחקים לסירוגין.
כל שחקן, בתורו, לוקח מהקופה בין 1 ל־10 גולות, לבחירתו. המנצח הוא השחקן שלוקח את הגולה האחרונה.
כתבו אלגוריתם שמשחק את המשחק בתור המחשב, נגד מתחרה אנושי.
בתחילת המשחק מקבל האלגוריתם כקלט את N ומחליט אם הוא רוצה לשחק ראשון או שני.
לאחר מכן, בכל תור, האלגוריתם מקבל כקלט את המהלך של המתחרה שלו ומחשב ומחזיר את המהלך שלו.
האלגוריתם שלכם חייב לנצח תמיד.
"""

import time


class TakeBallsGame:
    def __init__(self, num_balls, min_take, max_take, player1, player2):
        self.num_balls = num_balls
        self.min_take = min_take
        self.max_take = max_take
        self.players = (player1, player2)

    def play(self):
        print('Playing with {} balls. Each turn takes {}-{} balls.'.format(self.num_balls,
                                                                           self.min_take,
                                                                           self.max_take))
        print('{} vs. {}'.format(self.players[0], self.players[1]))
        cur_player = 0
        game_over = False
        while not game_over:
            print('There are currently {} balls.'.format(self.num_balls))
            time.sleep(1)
            choice = self.players[cur_player].play(self)
            self.num_balls -= choice
            print('{} took {} balls.'.format(self.players[cur_player], choice))
            if self.num_balls == 0:
                print('No more balls. {} won!!!'.format(self.players[cur_player]))
                game_over = True
            cur_player = 1 - cur_player  # toggle 'cur_player' between 0 and 1


class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class HumanPlayer(Player):
    def play(self, game: TakeBallsGame):
        while True:
            user_input = input('{} - {} balls left. Choose number between {}-{}: '.format(self.name,
                                                                                          game.num_balls,
                                                                                          game.min_take,
                                                                                          game.max_take))
            try:
                choice = int(user_input)
                if (choice >= game.min_take) and (choice <= game.max_take):
                    break
            except ValueError:
                pass
        return choice


class OptimalPlayer(Player):
    def play(self, game: TakeBallsGame):
        remainder = game.num_balls % (game.max_take + game.min_take)
        if remainder > 0:
            return remainder
        else:
            return game.min_take


def main():
    num_balls = int(input('How many balls you want to play? '))
    min_take = int(input('Minimal number to take in each turn: '))
    max_take = int(input('Maximal number to take in each turn: '))
    player1_name = input('First player name (press <Enter> for computer player): ')
    if player1_name == '':
        player1 = OptimalPlayer('Computer1')
    else:
        player1 = HumanPlayer(player1_name)
    player2_name = input('First player name (press <Enter> for computer player): ')
    if player2_name == '':
        player2 = OptimalPlayer('Computer2')
    else:
        player2 = HumanPlayer(player2_name)
    game = TakeBallsGame(num_balls, min_take, max_take, player1, player2)
    game.play()


main()
