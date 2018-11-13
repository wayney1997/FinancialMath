import numpy as np
import matplotlib.pyplot as plt

stock_data_f = open('data.txt','r')
stock_data = []
dS = []

for line in stock_data_f :
    stock_data.extend([float(i) for i in line.split()])

for i in stock_data :
    dS.append(np.log(i+1)-np.log(i))

vol = np.std(dS)
drift = np.mean(dS)+0.5*vol*vol

T=2
dt=0.01
t=np.arange(0,T,dt)
stock=np.zeros(len(t))
stock[0]=stock_data[-1]

for n in range(1,100):
    x=np.random.normal(0,1,len(t))
    for i in range(0,len(t)-1):
        stock[i+1]=stock[i]*np.exp(drift*dt+vol*np.sqrt(dt)*x[i])
    plt.plot(t,stock)

plt.show()
