from baccarat.player import Player
from baccarat.bet import Bet
from baccarat.martingale import Martingale
andrew = Player("M")

x = Martingale(andrew)
for i in range(0,100):
    x.play()
print(andrew.wallet)


print(andrew.max_wallet)
print(andrew.min_wallet)