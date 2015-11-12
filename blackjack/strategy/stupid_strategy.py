from blackjack.strategy.abstract_player_strategy import AbstractPlayerStrategy
from blackjack.strategy.const.actions import Actions


class StupidStrategy(AbstractPlayerStrategy):

    def handle_registration_info(self, registrationInfo):
        self.playerId = registrationInfo['playerId']
        self.seatNum = registrationInfo['seatNum']
        print 'assigned playerId: {}'.format(self.playerId)

    def handle_game_info(self, gameInfo):
        pass

    def handle_error(self, error):
        print error

    def get_bet_amount(self):
        self.splits = 0
        return 10

    def get_action(self, hand):
        value = hand['handValue']
        if len(hand['cards']) == 2:
            if value == 11:
                return Actions.DOUBLE
            if hand['cards'][0]['rank'] == hand['cards'][1]['rank'] and self.splits < 2:
                self.splits += 1
                return Actions.SPLIT
        elif value < 17:
            return Actions.HIT
        else:
            return Actions.STAND

    def get_name(self):
        return 'Max'

    def get_seat_num(self):
        return self.seatNum

    def get_player_id(self):
        return self.playerId