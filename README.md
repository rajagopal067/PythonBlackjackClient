# PythonBlackjackClient
Skeleton Blackjack client written in Python for the [blackjack server](https://github.com/chadtomas/Blackjack)

## Stuff you need
#### python 2.7
get it [here](https://www.python.org/download/releases/2.7/)
#### pip
`wget https://bootstrap.pypa.io/get-pip.py && sudo python get-pip.py`
#### Some dependencies
`sudo pip install ws4py`


`sudo pip install stompest`


## What to do with this code
This is a skeleton client. All of the stomp/websocket code is written for you, you just need to implement the blackjack strategy. There is an abstract class `blackjack.strategy.abstract_player_strategy.AbstractBlackjackStrategy` that you should subclass to accomplish this. Override all of the methods in there, adding whatever properties/logic you need. Take a look at `blackjack.strategy.stupid_strategy.StupidStrategy` to get a feel for it. Once you have your class, edit `application.py` to use your strategy instead of `StupidStrategy`. Host and port are configurable in `config.py`.
