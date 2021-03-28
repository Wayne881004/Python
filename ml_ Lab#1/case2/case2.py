import numpy as np 
import random
import math


Training_file = open("data2.txt","r")

Y = list()
Train_y = list()
X0 = list()
X1 = list()
X2 = list()
X3 = list()
X4 = list()
Epoch = int(0)
W0 = random.random()
W1 = random.random()
W2 = random.random()
W3 = random.random()
W4 = random.random()
MaxN = int(1000)
Error = float(1000)
Learning_Rate = float(1)
Amount = int(0)
tmp = float(0)

def Read_file(): 
    global Amount
    for i in Training_file.readlines():
        a, b, c, d, e = i.split()
        X0.append(int(1))
        X1.append(float(a))
        X2.append(float(b))
        X3.append(float(c))
        X4.append(float(d))
        Y.append(float(e))
        Amount += 1
        
def Gradient_descent():
    global Epoch, MaxN, Amount, Error, tmp, Learning_Rate
    global X0, X1, X2, X3, X4
    global W0, W1, W2, W3, W4
    while (Epoch < MaxN):
        tmp = 0
        for i in range(Amount): 
            W0 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i])) * X0[i]
            W1 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i])) * X1[i]
            W2 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i])) * X2[i]
            W3 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i])) * X3[i]
            W4 += Learning_Rate * (Y[i] - (W0 * X0[i] + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i])) * X4[i]
        Epoch += 1
        for i in range(Amount):
            y_hat = W0 * X0[i] + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i]
            tmp += math.pow(Y[i] - y_hat,2)
        tmp /= Amount
        if(tmp < Error):
            break

def Update():
    global Amount
    global Train_y, X1, X2, X3, X4
    global W0, W1, W2, W3, W4
    for i in range(Amount): 
        Train_y.append(W0 + W1 * X1[i] + W2 * X2[i] + W3 * X3[i] + W4 * X4[i])
   
if __name__ == '__main__':
    Read_file()
    Gradient_descent()   
    Update()
    print("{} {} {} {} {}".format(W0,W1,W2,W3,W4))
    print("{}".format(W0 + W1 * 6.8 + W2 * 210 + W3 * 0.402 + W4 * 0.739))