import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime, argparse

parser = argparse.ArgumentParser()
parser.add_argument("symbol",help="NASDAQ ticker symbol")
parser.add_argument("T",type=int,help="length of total time interval")
parser.add_argument("dt",type=float,help="time interval to iterate")
parser.add_argument("N",type=int,help="number of sample paths")
args = parser.parse_args()

title = 'NASDAQ:'+ args.symbol

start = datetime.datetime.now() - datetime.timedelta(days=5*365)
end = datetime.date.today()
stock_data = web.DataReader(args.symbol,'iex',start,end)['close'].tolist()
dS = []

for i in stock_data :
    dS.append(np.log(i+1)-np.log(i))

vol = np.std(dS)
drift = np.mean(dS)+0.5*vol*vol

t=np.arange(0,args.T+args.dt,args.dt)
stock=np.zeros(len(t))
stock[0]=stock_data[-1]

for n in range(1,args.N):
    x=np.random.normal(0,1,len(t))
    for i in range(0,len(t)-1):
        stock[i+1]=stock[i]*np.exp(drift*args.dt+vol*np.sqrt(args.dt)*x[i])
    plt.plot(t,stock)

plt.title(title)
plt.xlabel('Day(s) after current time')
plt.ylabel('USD($)')    
plt.show()
