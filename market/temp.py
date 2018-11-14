import pandas as pd
import pandas_datareader.data as web
import datetime as dt

start = dt.datetime(2018,3,26)
end = dt.datetime(2018,3,29)

tickers = ['IBM','INTC']

df = pd.concat([web.DataReader(ticker,'iex', start, end) for ticker in tickers]).reset_index()
print(df)
