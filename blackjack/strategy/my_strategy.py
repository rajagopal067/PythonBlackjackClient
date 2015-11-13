from blackjack.strategy.abstract_player_strategy import AbstractPlayerStrategy
from blackjack.strategy.const.actions import Actions


class MyStrategy(AbstractPlayerStrategy):

    def handle_registration_info(self, registrationInfo):
        self.playerId = registrationInfo['playerId']
        self.seatNum = registrationInfo['seatNum']
        print 'assigned playerId: {}'.format(self.playerId)

    def handle_game_info(self, gameInfo):
        print gameInfo

    def handle_error(self, error):
        print error

    def get_bet_amount(self):
        self.splits = 0
        return 10

    def has2_10pointcards(self,hand):
        cards = hand['cards']
        count_10pointcards = 0
        for card in cards:
            if card['cardValue']==10:
                count_10pointcards +=1
        if count_10pointcards > 1 and self.splits < 2:
            return True
        else:
            return False

    def get_action(self, hand):
        value = hand['handValue']
        if len(hand['cards']) == 2:
            if value < 5:
                return Actions.DOUBLE
            elif value < 12:
                return Actions.HIT
            else:
                return Actions.STAND
        elif value > 21:
            return Actions.SURRENDER
        else:
            if self.has2_10pointcards(hand):
                self.splits += 1
                return Actions.SPLIT
            return Actions.STAND

    def get_name(self):
        return 'Max'

    def get_seat_num(self):
        return self.seatNum

    def get_player_id(self):
        return self.playerId