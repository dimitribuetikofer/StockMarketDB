import time
import datetime
import pandas as pd
import os

tickers = ['ABBN.SW',
            'ALC.SW',
            'CSGN.SW',
            'GEBN.SW',
            'GIVN.SW',
            'HOLN.SW',
            'LOGN.SW',
            'LONN.SW',
            'NESN.SW',
            'NOVN.SW',
            'PGHN.SW',
            'CFR.SW',
            'ROG.SW',
            'SGSN.SW',
            'SIKA.SW',
            'SLHN.SW',
            'SREN.SW',
            'SCMN.SW',
            'UBSG.SW',
            'ZURN.SW']

period1 = int(time.mktime(datetime.datetime(2015,1,1,23,59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2022,8,11,23,59).timetuple()))
interval = '1d'

df_stockdata = pd.DataFrame(columns = ["Date", "Ticker", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

for ticker in tickers:
    url = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'
    temp_df = pd.read_csv(url)
    temp_df.insert(1, 'Ticker', ticker)
    print(temp_df)
    df_stockdata = pd.concat([df_stockdata, temp_df], ignore_index=True, sort = False)

if not os.path.exists('./Data'):
    os.mkdir('./Data')
df_stockdata.to_csv('Data/stockdata.csv', index=False)