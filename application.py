from blackjack.blackjack_client import BlackjackClient
from blackjack.strategy.stupid_strategy import StupidStrategy
from blackjack.strategy.my_strategy import MyStrategy
import config

if __name__ == '__main__':
    strategy = MyStrategy()
    client = BlackjackClient('ws://{}:{}/connectPython'.format(config.host, config.port), strategy)
    try:
        client.run_forever()
    except KeyboardInterrupt:
        client.close()




