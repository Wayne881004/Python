import numpy as np 
import random
import math
import matplotlib.pyplot as plt

Training_file = open("data1.txt","r")

Y = list()
Train_y = list()
X0 = list()
X1 = list()
Epoch = int(0)
W0 = random.random()
W1 = random.random()
MaxN = int(1000)
Error = float(10)
Learning_Rate = float(1)
Amount = int(0)
tmp = float(0)

def Read_file(): 
    global Amount
    for i in Training_file.readlines():
        a, b = i.split()
        X0.append(int(1))
        X1.append(int(a))
        Y.append(float(b))
        Amount += 1
        
def Gradient_descent():
    global Epoch, MaxN, Amount, Error, tmp, Learning_Rate
    global X0, X1, W0, W1
    while (Epoch < MaxN):
        tmp = 0
        for i in range(Amount): 
            W0 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i])) * X0[i]
            W1 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i])) * X1[i]
            
        Epoch += 1
        for i in range(Amount):
            y_hat = W0 * X0[i] + W1 * X1[i] 
            tmp += math.pow(Y[i] - y_hat,2)
        tmp /= Amount
        if(tmp < Error):
            break

def Update():
    global Amount
    global W0, W1, X1, Train_y
    for i in range(Amount): 
        Train_y.append(W0 + W1 * X1[i])
   
if __name__ == '__main__':
    Read_file()
    Gradient_descent()   
    Update()
    print("{} {}".format(W0,W1))
    plt.plot(X1,Y,".",color = "r")
    plt.plot(X1,Train_y,color = "b")
    plt.xlabel("Claims")
    plt.ylabel("Total payment")
    plt.title("learning rate = {}".format(Learning_Rate))
    plt.savefig("{}.png".format(Learning_Rate))
    plt.show()