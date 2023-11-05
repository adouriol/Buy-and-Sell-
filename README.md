# Buy and Sell
This code allows you to buy and sell on the Binance API.
You can choose the strategy that you want to follow in my case I used a very simple EMA strategy.

# Usage
This code works like a script you just have to python main.py and it will start running.
You can change all the parameters in config.py to adjust to your needs.

# Structure
The code contains an main.py where all the logic starts.
It will go throw the crypto you want to check and will create an object named candlestick containing the data, the crypto name, the depth and the client.
The data will be treated and it will ad some financial indicators.
Then if the condition are met it will buy or sell. In the case that the condition are not covered. The script will wait one hour.
