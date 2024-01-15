from baccarat.martingale import Martingale
from baccarat.player import Player


class MartingaleSim:
    def __init__(self, players, hands):
        self.players = players
        self.hands = hands
        self.running_total = 0
        self.complete_loss = 0
        self.highest_win = 0
        self.history = {}
        self.highest_win_buyback = 0
        self.win_streak = 0
        self.lose_streak= 0

    def sim(self):
        for i in range(self.players):
            x = Player("M")
            y = Martingale(x)
            for j in range(self.hands):
                y.play()
                if y.player.wallet <= 0:
                    self.complete_loss += 1
                    self.players -=1
                    break
                if j in self.history:

                    self.history[j] += (y.player.wallet - (12800 * (4 - y.player.buy_backs)))/self.players
                else:
                    self.history[j] = (y.player.wallet - (12800 * (4 - y.player.buy_backs)))/self.players

            self.running_total += y.player.wallet
            if (y.player.wallet - (12800 * (4 - y.player.buy_backs))) > self.highest_win:

                self.highest_win = y.player.wallet - (12800 * (4 - y.player.buy_backs))
                self.highest_win_buyback = 3 - y.player.buy_backs

            self.win_streak = max(self.win_streak, y.player.best_win_streak)
            self.lose_streak = max(self.lose_streak, y.player.worst_loss_streak)

