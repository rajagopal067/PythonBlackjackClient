from ws4py.client.threadedclient import WebSocketClient
from stompest.protocol import StompSession, StompSpec, StompParser
import json
import time
from blackjack.strategy.const.game_status import GameStatus
import config



class BlackjackClient(WebSocketClient):
    PLAYER_QUEUE = '/queue/player*'
    PLAYERS_QUEUE = '/queue/players*'
    ERRORS_QUEUE = '/queue/errors*'
    GAME_TOPIC = '/topic/game'
    queues = [PLAYER_QUEUE, PLAYERS_QUEUE, ERRORS_QUEUE, GAME_TOPIC]




    def __init__(self, url, playerStrategy):
        super(BlackjackClient, self).__init__(url)
        self.tokens = {}
        self.strategy = playerStrategy
        self.parser = StompParser(StompSpec.VERSION_1_1)
        self.session = StompSession(StompSpec.VERSION_1_1)
        self.connect()
        while self.session.state != 'connected':
            time.sleep(.1)
        self.__subscribe_to_queues()
        self.send_stomp('/app/register', json.dumps({'name': self.strategy.get_name()}))


    def __subscribe_to_queues(self):
        id = 0
        for queue in self.queues:
            subscribeFrame, token = self.session.subscribe(queue, headers={'id': id})
            self.tokens[queue] = token
            # print "sending frame\n" + str(subscribeFrame)
            self.send(str(subscribeFrame))
            id += 1


    def __get_player_from_gameinfo(self, gameInfo):
        if len(gameInfo['players']) == 0:
            return None
        for player in gameInfo['players']:
            if player['seatNum'] == self.strategy.seatNum and player['name'] == self.strategy.get_name():
                return player
        for player in gameInfo['players']:
            if player['name'] == self.strategy.get_name():
                return player
        raise Exception('player was removed from the game')


    def opened(self):
        print "opened"
        connectFrame = self.session.connect(host='{}:{}'.format(config.host, config.port))
        # print "sending frame\n" + str(connectFrame)
        self.send(str(connectFrame))


    def send_stomp(self, destination, message):
        sendFrame = self.session.send(destination, message)
        # print "sending frame\n" + str(sendFrame)
        self.send(str(sendFrame))


    def closed(self, code, reason=None):
        print "Closed down", code, reason


    def received_message(self, m):
        self.parser.add(str(m))
        frame = self.parser.get()
        print dict(frame)

        if frame.command == StompSpec.CONNECTED:
            self.session.connected(frame)
            return

        destination = frame.headers['destination']
        if destination == '/user/queue/player':
            self.strategy.handle_registration_info(json.loads(frame.body))
            bet = self.strategy.get_bet_amount()
            self.send_stomp('/app/bet', json.dumps({'playerId': self.strategy.get_player_id(), 'betAmount': bet}))

        elif destination == '/user/queue/players' or destination == '/topic/game':
            gameInfo = json.loads(frame.body)
            self.strategy.handle_game_info(gameInfo)
            player = self.__get_player_from_gameinfo(gameInfo)
            if player is None:
                pass
            if gameInfo['gameStatus'] == GameStatus.BETTING_ROUND and not player['betInForNextRound']:
                bet = self.strategy.get_bet_amount()
                self.send_stomp('/app/bet', json.dumps({'playerId': self.strategy.get_player_id(), 'betAmount': bet}))
            elif gameInfo['gameStatus'] == GameStatus.HAND_IN_PROGRESS:
                handNum = 0
                for hand in player['hands']:
                    if hand['turn']:
                        action = self.strategy.get_action(hand)
                        self.send_stomp('/app/action', json.dumps({'playerId': self.strategy.get_player_id(), 'handNum': handNum, 'action': action}))
                        break
                    handNum += 1

        elif destination == '/user/queue/errors':
            self.strategy.handle_error(json.loads(frame.body))
