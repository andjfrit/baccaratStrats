from .game import Game



class Player:
    def __init__(self, strat):
        self.strat = strat
        self.wallet = 12800
        self.bet_number = 0
        self.win_num = 0
        self.loss_num = 0
        self.tie_num = 0
        self.win_last_game = True
        self.second_win_last_game = True
        self.tie_last_tame = False
        self.last_bet = 0
        self.max_wallet = 12800
        self.min_wallet = 12800
        self.buy_backs = 3
        self.best_win_streak = 0
        self.worst_loss_streak = 0
        self.current_win_streak = 0
        self.current_loss_streak = 0


