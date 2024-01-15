from .game import Game
from .player import Player
from .bet import Bet


class Martingale:
    def __init__(self, player: Player):
        self.player = player
        self.bet_history = []

    def play(self):
        bet = Bet
        if self.player.win_last_game:
            bet = Bet(1, 100)
            if self.player.wallet < 100:
                print("dont have enough money")
                print(self.player.wallet)
                print(self.player.buy_backs)
                if (self.player.buy_backs>0):
                    self.player.buy_backs-=1
                    self.player.wallet += 12800
                else:
                    return 0

            self.bet_history.append(bet)
            self.player.last_bet = 100
            self.player.wallet -= 100
            self.player.bet_number += 1

        else:
            if self.player.second_win_last_game:
                newwager = 100
            else:
                newwager = (self.player.last_bet * 2)
            bet = Bet(0, newwager)
            if self.player.wallet < newwager:
                if self.player.buy_backs> 0:
                    self.player.buy_backs -= 1
                    self.player.wallet += 12800
                    if self.player.second_win_last_game:
                        newwager = 100
                    else:
                        newwager = (self.player.last_bet * 2)
                else:
                    newwager = self.player.wallet
                    bet = Bet(0, newwager)

            self.player.wallet -= newwager
            self.bet_history.append(bet)
            self.player.last_bet = newwager
            self.player.bet_number += 1


        game = Game()
        result = game.play_round()

        if result == 2:

            self.player.tie_num += 1
            self.player.wallet += bet.amount
            self.player.last_bet = self.player.last_bet/2

        elif result == bet.favorite:

            self.player.wallet += (bet.amount * 2)
            self.player.second_win_last_game = self.player.win_last_game
            self.player.win_last_game = True
            self.player.win_num += 1
            self.player.max_wallet = max(self.player.max_wallet, self.player.wallet)
            self.player.current_win_streak += 1
            self.player.current_loss_streak = 0
            self.player.best_win_streak = max(self.player.current_win_streak,self.player.current_win_streak)
        else:
            self.player.second_win_last_game = self.player.win_last_game
            self.player.win_last_game = False
            self.player.loss_num += 1
            self.player.min_wallet = min(self.player.min_wallet, self.player.wallet)
            self.player.current_win_streak = 0
            self.player.current_loss_streak += 1
            self.player.worst_loss_streak = max(self.player.current_loss_streak,self.player.current_loss_streak)
        return self.player.wallet

