import numpy as np
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt
import datetime, argparse


parser = argparse.ArgumentParser(description="Montecarlo simulation code for NASDAQ asset paths using data from IEX. Asset price model based on geometrical Brownian asset model under simple efficient market assumptions.")
parser.add_argument("symbol",help="NASDAQ ticker symbol")
parser.add_argument("T",type=int,help="time to expiry (days)")
parser.add_argument("dt",type=float,help="length of the step to iterate until expiry")
parser.add_argument("N",type=int,help="number of sample paths")
parser.add_argument("-s","--save",action="store_true",help="save simulation data as csv, format: date_symbol_N_T_dt")
args = parser.parse_args()

start = datetime.datetime.now() - datetime.timedelta(days=5*365)
end = datetime.date.today()

if args.save:
    savelist = []
    filename = str(end) + '_' + args.symbol + '_' + str(args.N) + '_' + str(args.T) + '_' + str(args.dt)+'.csv'
    print("saving ",args.N," simulation results")

title = 'NASDAQ:'+ args.symbol
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
    df.to_csv(filename)

plt.title(title)
plt.xlabel('Day(s) after current time')
plt.ylabel('USD($)')    
plt.show()
