from .deck import Deck


def rank_int(card):
    try:
        return int(card.rank)
    except ValueError:
        if card.rank == "A":
            return 1
        return 0


def calculate_score(hand):
    count = 0
    for i in hand:
        count += rank_int(i)
    return count % 10


class Game:
    def __init__(self):
        # Initialize game components like the deck and player/banker hands
        self.deck = Deck()
        self.player_hand = []
        self.banker_hand = []
        self.player_third = False

    def deal_initial_cards(self):
        self.player_hand.append(self.deck.deal())
        self.banker_hand.append(self.deck.deal())
        self.player_hand.append(self.deck.deal())
        self.banker_hand.append(self.deck.deal())

    def player_turn(self):
        first = rank_int(self.player_hand[0])
        second = rank_int(self.player_hand[1])

        if (first + second) % 10 <= 5:
            self.player_hand.append(self.deck.deal())
            self.player_third = True

            third = rank_int(self.player_hand[2])



    def banker_turn(self):
        first = rank_int(self.banker_hand[0])
        second = rank_int(self.banker_hand[1])

        if not self.player_third:

            if (first + second) % 10 <= 5:
                self.banker_hand.append(self.deck.deal())

        else:
            player_third = rank_int(self.player_hand[2])
            if (first + second) % 10 <= 2:
                self.banker_hand.append(self.deck.deal())
            if (first + second) % 10 == 3:
                if player_third != 8:
                    self.banker_hand.append(self.deck.deal())
            if (first + second) % 10 == 4:
                if player_third not in {0,1,8,9}:
                    self.banker_hand.append(self.deck.deal())

            if (first + second) % 10 == 5:
                if player_third in {4,5,6,7}:
                    self.banker_hand.append(self.deck.deal())
            if (first + second) % 10 == 6:
                if player_third in {6,7}:
                    self.banker_hand.append(self.deck.deal())

    def determine_winner(self):
        player_score = calculate_score(self.player_hand)
        banker_score = calculate_score(self.banker_hand)
        if player_score > banker_score:

            return 0
        elif player_score < banker_score:
            return 1
        else:
            return 2

    def play_round(self):
        self.deal_initial_cards()
        player_total = calculate_score(self.player_hand)
        banker_total = calculate_score(self.banker_hand)

        if player_total >= 8 or banker_total >= 8:
            return self.determine_winner()
        else:
            self.player_turn()
            self.banker_turn()

            return self.determine_winner()







