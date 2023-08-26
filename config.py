from smartapi import SmartConnect

def ord1(API_KEY_MJ='', USERID_MJ="", PASSWORD_MJ=""):
    api_key = API_KEY_MJ
    obj = SmartConnect(api_key=api_key, )
    userid = USERID_MJ
    password = PASSWORD_MJ
    data = obj.generateSession(userid, password)
    print(data['data'])
    if data['data']:
        refreshToken = data['data']['refreshToken']
        feedToken = obj.getfeedToken()
        userProfile = obj.getProfile(refreshToken)
        return obj

def give_param(TYPE,SYMBOL,TOKEN,PRICE,QUANTITY,ORDERTYPE,VARIETY,EXCHANGE):
    param ={
        "variety": VARIETY,
        "tradingsymbol": SYMBOL,
        "symboltoken": str(TOKEN),
        "transactiontype": TYPE,
        "exchange": EXCHANGE,
        "ordertype": ORDERTYPE,
        "producttype": "INTRADAY",
        "duration": "DAY",
        "triggerprice": str(PRICE),
        "price": "0.0",
        "squareoff": "0.0",
        "stoploss": "0.0",
        "quantity": str(QUANTITY),
        }
    return param