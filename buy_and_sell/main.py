from config import config
from tools import utils 
from binance.client import Client
from data.candlestick import Candlestick
from time import sleep, time
import datetime

api_secret, api_key = utils.get_api_key()
client = Client(api_key,api_secret)
crypto = config.cryptocurrency
 
while True:
        t0 = time()
        canlde_to_work = Candlestick(utils.get_candlestick(crypto), crypto, config.n, client)
        canlde_to_work.treatment()
        canlde_to_work.signal_generator()              
        time_to_sleep = max(0, config.interval - (time()-t0)) 
        
        if time_to_sleep <0:
            time_to_sleep = (60-datetime.now().minute)*60
            
        print(f"Waiting for {round(time_to_sleep)} s")
        sleep(time_to_sleep)   