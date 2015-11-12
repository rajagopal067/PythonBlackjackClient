import json
from threading import Thread
from blackjack.blackjack_client import BlackjackClient
from blackjack.strategy.stupid_strategy import StupidStrategy
import config

if __name__ == '__main__':
    strategy = StupidStrategy()
    client = BlackjackClient('ws://{}:{}/connectPython'.format(config.host, config.port), strategy)
    try:
        client.run_forever()
    except KeyboardInterrupt:
        client.close()




