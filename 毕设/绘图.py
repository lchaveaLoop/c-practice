import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False
plt.rcParams["font.sans-serif"]=["SimHei"]

def sigmoid(x):
    return (1.0/1+np.exp(-x))

sigmoid_inputs = np.arange(-10,10)
sigmoid_outputs=sigmoid(sigmoid(sigmoid_inputs))
def draw_sigmoid(sigmoid_inputs,sigmoid_outputs):
    plt.plot(sigmoid_inputs,sigmoid_outputs,label='1/(1+e^(-x) )')
    plt.plot(sigmoid_inputs,sigmoid_outputs)
    plt.legend()
    plt.xlabel("Sigmoid函数输入")
    plt.ylabel("Sigmoid函数输出")
    l=plt.show()
    return l
# draw_sigmoid(sigmoid_inputs,sigmoid_outputs)

def softmax(x):
    orig_shape=x.shape
    if len(x.shape)>1:
        #Matrix
        #shift max whithin each row
        constant_shift=np.max(x,axis=1).reshape(1,-1)
        x-=constant_shift
        x=np.exp(x)
        normlize=np.sum(x,axis=1).reshape(1,-1)
        x/=normlize
    else:
        #vector
        constant_shift=np.max(x)
        x-=constant_shift
        x=np.exp(x)
        normlize=np.sum(x)
        x/=normlize
    assert x.shape==orig_shape
    return x


softmax_inputs = np.arange(-10,10)
softmax_outputs=softmax(softmax_inputs)
def draw_softmax(softmax_inputs,softmax_outputs):
    plt.plot(softmax_inputs, softmax_outputs)
    # plt.legend()
    plt.xlabel("Softmax函数输入")
    plt.ylabel("Softmax函数输出")
    l=plt.show()
    return l
# draw_softmax(softmax_inputs,softmax_outputs)

def relu(x):
    return np.where(x<0,0,x)

x=np.arange(-10,10,0.1)
y=relu(x)
def draw_relu(x,y):
    plt.plot(x,y,label='f(x)=max(0,x)')
    plt.legend()
    plt.xlabel("relu函数输入")
    plt.ylabel("relu函数输出")
    return plt.show()
draw_relu(x,y)