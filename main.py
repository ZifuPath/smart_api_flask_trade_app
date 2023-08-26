from flask import render_template,Flask,request
from config import *
import pandas as pd
app = Flask(__name__)
df1 = pd.read_csv('dataset/token.csv')
lst1 = list(df1.symbol.unique())
df = pd.read_csv('dataset/nifty.csv')
lst = list(df.symbol.unique())
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main/',methods=['GET'])
def welcome():
    return render_template('main.html', stocklist=lst)
obj = ord1()

@app.route('/main/',methods=['POST'])
def order():
    data=request.form
    type = data.get('Action')
    symbol = data.get('stock')
    if symbol:
        df.query(f'symbol== "{symbol}"', inplace=True)
        token = int(df.token.iloc[0])
        qty = int(48000/int(df.price.iloc[0]))
        print(token,qty)
        param = give_param(TYPE=type,
                           SYMBOL=symbol,
                           TOKEN=token,
                           PRICE=0,
                           QUANTITY=qty,
                           ORDERTYPE= 'MARKET',
                           VARIETY='NORMAL',
                           EXCHANGE='NSE')
        obj.placeOrder(param)
        msg = f'{symbol} - {type} - qty - {qty}'
        return render_template('main.html',stocklist=lst,msg = msg)
    return render_template('main.html', stocklist=lst)

@app.route('/bank/',methods=['GET','POST'])
def bank_nifty():
    if request.method=='POST':
        data=request.form
        type = data.get('Action')
        symbol = data.get('stock')
        if symbol:
            df.query(f'symbol== "{symbol}"', inplace=True)
            token = int(df.token.iloc[0])
            qty = 25
            param = give_param(TYPE=type,
                               SYMBOL=symbol,
                               TOKEN=token,
                               PRICE=0,
                               QUANTITY=qty,
                               ORDERTYPE= 'MARKET',
                               VARIETY='NORMAL',
                               EXCHANGE='NFO')
            obj.placeOrder(param)
            msg = f'{symbol} - {type} - qty - {qty}'
            return render_template('main.html',stocklist=lst1,msg = msg)
        return render_template('main.html', stocklist=lst1)
    return render_template('main.html', stocklist=lst1)
if __name__ == '__main__':
    #df3 = pd.read_csv('dataset/nifty.csv')
    
    #for i in range(len(df3)):
        #ltp = obj.ltpData(exchange='NSE',tradingsymbol=df.symbol.iloc[i],symboltoken=str(df.token.iloc[i]))
        #ltp = ltp['data']['ltp']
        #df3.price.iloc[i] = ltp
        #print(df3.symbol.iloc[i],df.price.iloc[i])
    #df3.to_csv('dataset/nifty.csv',index=False)
    app.run(debug=True)
