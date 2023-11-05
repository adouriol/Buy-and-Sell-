from finta import TA
import pandas as pd
from config import config
from tools import utils, make_orders

class Candlestick:
    
    def __init__(self,data, crypto, n, client):
        self.data = data
        self.crypto = crypto
        self.n = n
        self.bought = False
        self.client = client

    def treatment(self):
        # data treatment to optain EMA values and shorten the dataset
        df = self.data  
        df["open"] = df["open"].astype('float')
        df["close"] = df["close"].astype('float')
        df["high"] = df["high"].astype('float')
        df["low"] = df["low"].astype('float')
        df["EMA_20"] = TA.EMA (df,20)
        df['EMA_50'] = TA.EMA(df,50)
        df['EMA_200'] = TA.EMA(df,200)
        df.fillna(0, inplace= True)
        df= df.reset_index()
        df= df.drop(columns=['index','level_0','closetime','quoteassetvolume','ntrades','takerbuybaseassetvolume','takerbuyquoteassetvolume','delete_me_pls'])
        data= df.iloc[-self.n:]
        index = pd.Index(range(-self.n+1, 1, 1))
        self.data = data.set_index(index)
    
    def signal_generator(self):
        # Buy or sell if the conditions are met
        
        def signal_buy():
            if utils.buy_condition(self.data):
                amount = config.capital
                make_orders.insert_money(self.client,make_orders.get_price_crypto(self.client,self.crypto), amount, self.crypto)
                self.bought = True
                
        def signal_sell():
            if utils.sell_condition(self.data):
                amount_to_sell = make_orders.get_quantity(self.client, self.crypto)
                make_orders.sell_money(self.client,make_orders.get_price_crypto(self.client,self.crypto), amount_to_sell, self.crypto)
                self.bought = False
        if self.bought: return signal_sell()
        else : return signal_buy()
        
    
         
        
        
        
        
        
        
        

#create sub-class to buy or not