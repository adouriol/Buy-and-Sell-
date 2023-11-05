import math

def get_quantity(client,asset):
    # Get amount of any cryptocurrency

    return float(client.get_asset_balance(asset=asset)['free'])

def get_price_crypto(client,symbol):
    # Get price of any cryptocurrency
    return float(client.get_symbol_ticker(symbol=symbol)['price'])

def insert_money(client, price_buy,quantity,symbol): 
    # Place a buy order
    client.create_order(
            symbol=symbol,
            side='BUY',
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price_buy
        )
    return print(f'order place at {price_buy} for {quantity} to buy')   

def sell_money(client, price_sell,quantity,symbol):
    #Place a sell order 
    client.create_order(
            symbol=symbol,
            side='SELL',
            type='LIMIT',
            timeInForce='GTC',
            quantity=quantity,
            price=price_sell)
    
    return print(f'order place at {price_sell} for {quantity} to sell')