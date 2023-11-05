import json 
from os.path import expanduser, join
import pandas as pd
import requests 
from config import config

def get_api_key(secret=False) -> str:
    #Get secret api key from .binance_api_secrets file stored in current directory 
    secret_path = join(expanduser('~'), '.binance_api_secrets')
    with open(secret_path) as f:
        keys = json.load(f)
    key,secret = keys.get('key') ,keys.get('secret')
    return secret, key

def get_candlestick(crypto):
    
    tick_interval= config.candlestick_interval
    url = ''.join([config.url_api[0],crypto,config.url_api[1], tick_interval])
    data = requests.get(url).json()
    df= pd.DataFrame(data)
    df.rename(
        columns={0:"opentime",
                1:"open",
                2:"high",
                3:"low",
                4:"close",
                5:"Volume",
                6:"closetime",
                7:"quoteassetvolume",
                8:"ntrades",
                9:"takerbuybaseassetvolume",
                10:"takerbuyquoteassetvolume",
                11:'delete_me_pls'},
        inplace=True)
    df.reset_index(inplace= True)
    return df 

def buy_condition(data):
    if data['EMA_20'][-1] > data['EMA_50'][-1] and data['EMA_20'][-2] > data['EMA_50'][-2] and data['EMA_200'][-1]< data['EMA_50'][-1]: return True
    else : return False
        
def sell_condition(data):
    if data['EMA_20'][-1] < data['EMA_50'][-1] and data['EMA_20'][-2] > data['EMA_50'][-2]: return True
    else: return False