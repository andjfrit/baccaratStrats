from .martingaleSim import MartingaleSim
import matplotlib.pyplot as plt
from baccarat.martingale import Martingale
from baccarat.player import Player



class GraphSim:
    def __init__(self, players, totalhands):
        self.players = int(players)
        self.totalhands = int(totalhands)
        self.interval = 1
        self.avg_winning_per_interval = {}

    def get_data(self):
        x = MartingaleSim(self.players,self.totalhands)
        x.sim()
        self.avg_winning_per_interval = x.history
        print(f"the number of players that lost it all including 3 buybacks {x.complete_loss}")
        print(f"the highest any player had at any point{x.highest_win}")
        print(f"but this fucker used this many buybacks: {x.highest_win_buyback}")
        print(f"The best and worst winstreaks for anyone were ... win streak: {x.win_streak} and loss streak of {x.lose_streak}")

    def create_graph(self):
        hands, averages = zip(*sorted(self.avg_winning_per_interval.items()))
        plt.plot(hands, averages)
        plt.xlabel("number of hands played")
        plt.ylabel("avg winning")
        plt.title("avg bac winning per hand per players")
        plt.grid(True)
        plt.show()
