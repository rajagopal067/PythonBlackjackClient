class AbstractPlayerStrategy:
    def handle_registration_info(self, registrationInfo):
        """
        this method is called when your player is registered
        :param registrationInfo: dict of registration information
        :return: nothing
        """
        raise NotImplementedError('class {} does not implement handle_registration_info()'.format(self.__class__.__name__))

    def handle_game_info(self, gameInfo):
        """
        this method is called whenever a player places a bet or executes an action
        :param gameInfo: dict representing the current status of the game
        :return: nothing
        """
        raise NotImplementedError('class {} does not implement handle_game_info()'.format(self.__class__.__name__))

    def handle_error(self, error):
        """
        any error broadcasted by the server will get passed into this method
        :param error: dict representing error
        :return: nothing
        """
        raise NotImplementedError('class {} does not implement handle_error()'.format(self.__class__.__name__))

    def get_bet_amount(self):
        """
        how much you'd like to bet this round
        :return: int wager amount - increment of 10
        """
        raise NotImplementedError('class {} does not implement get_bet_amount()'.format(self.__class__.__name__))

    def get_name(self):
        """
        :return: string player name
        """
        raise NotImplementedError('class {} does not implement get_name()'.format(self.__class__.__name__))

    def get_seat_num(self):
        """
        :return: seat number from registration info
        """
        raise NotImplementedError('class {} does not implement get_seat_num()'.format(self.__class__.__name__))

    def get_player_id(self):
        """
        :return: player id from registration info
        """
        raise NotImplementedError('class {} does not implement get_player_id()'.format(self.__class__.__name__))

    def get_action(self, hand):
        """
        returns an action that should be taken on the provided hand
        :param hand: dict representing the hand to take action on
        :return: blackjack.strategy.const.actions.Actions for which action you'd like to take
        """
        raise NotImplementedError('class {} does not implement get_action()'.format(self.__class__.__name__))