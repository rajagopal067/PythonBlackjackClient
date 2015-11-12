class AbstractPlayerStrategy:
    def handle_registration_info(self, registrationInfo):
        raise NotImplementedError('class {} does not implement handle_registration_info()'.format(self.__class__.__name__))

    def handle_game_info(self, gameInfo):
        raise NotImplementedError('class {} does not implement handle_game_info()'.format(self.__class__.__name__))

    def handle_error(self, error):
        raise NotImplementedError('class {} does not implement handle_error()'.format(self.__class__.__name__))

    def get_bet_amount(self):
        raise NotImplementedError('class {} does not implement get_bet_amount()'.format(self.__class__.__name__))

    def get_name(self):
        raise NotImplementedError('class {} does not implement get_name()'.format(self.__class__.__name__))

    def get_seat_num(self):
        raise NotImplementedError('class {} does not implement get_seat_num()'.format(self.__class__.__name__))

    def get_player_id(self):
        raise NotImplementedError('class {} does not implement get_player_id()'.format(self.__class__.__name__))

    def get_action(self, hand):
        raise NotImplementedError('class {} does not implement get_action()'.format(self.__class__.__name__))