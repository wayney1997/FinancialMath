import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime, argparse


parser = argparse.ArgumentParser()
parser.add_argument("symbol",help="NASDAQ ticker symbol")
parser.add_argument("T",type=int,help="length of total time interval")
parser.add_argument("dt",type=float,help="time interval to iterate")
parser.add_argument("N",type=int,help="number of sample paths")
parser.add_argument("-s","--save",action="store_true",help="save simulation data as csv")
args = parser.parse_args()

if args.save:
    savelist = []
    print("saving ",args.N," simulation results")

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

for n in range(0,args.N):
    stock = np.zeros(len(t))
    stock[0]=stock_data[-1]
    x=np.random.normal(0,1,len(t))
    for i in range(0,len(t)-1):
        stock[i+1]=stock[i]*np.exp(drift*args.dt+vol*np.sqrt(args.dt)*x[i])
    savelist.append(stock)
    plt.plot(t,stock)

if args.save:
    df = pd.DataFrame(savelist)
    df.to_csv("test.csv")

plt.title(title)
plt.xlabel('Day(s) after current time')
plt.ylabel('USD($)')    
plt.show()
