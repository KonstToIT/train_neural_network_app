#!/usr/bin/env python
# coding: utf-8

# In[142]:
import random as rd
import numpy as np
import copy
def sig(x):
    x_64=x.astype(float)
    return 1/(1+np.exp(-x_64))

# In[143]:
class model:
    """
        class for creating neural network objects
        Each object has 4 atributes. They are:
        arch-neural network's architecture
        cost-current value of cost function
        stop-flag for stopping training when necessary
        weights- current values of weights
    """
    
    def __init__(s,arch):#create model with specific architecture and random initialized weights and cost_value=1000
        
        s.arch=arch
        s.cost=1000
        s.stop=False
        s.weights=[
            np.array([
                [
                    rd.uniform(-0.5,0.5) for k in range(arch[i])
                ] for j in range(arch[i+1])
            ]) for i in range(len(arch)-1)
        ]
    
    
    def make_one_iteration(s,X,Y,previous_cost,lr=1,l=0.4):
        """
            This function realizes one epoch of training
            Input: model object,training set,targets,learning rate,regularization parameter
        """
        s.stop=False
        arch=s.arch
        weights=copy.deepcopy(s.weights)
        cap_deltas=[]
        for i in range(len(arch)-1):
            cap_deltas.append(np.array([[0 for k in range(arch[i])] for j in range(arch[i+1])]))
        sum_er=0
        for t in range(len(X)):
            #forward propagation
            a=[]
            z=[]
            for i in range(len(arch)):
                if i==0:
                    a.append(X[t].reshape(1,arch[0]))
                else:
                    z.append(np.matmul(a[i-1],weights[i-1].transpose()))
                    a.append(sig(z[i-1]))

            #backpropagation
            E_total=-Y[t]*np.log(a[len(arch)-1])-(1-Y[t])*np.log(1-a[len(arch)-1])
            sum_er+=E_total
            deltas=[]
            
            for i in range(len(arch)-1,0,-1): #calculating delta terms for each layer
                if i==len(arch)-1:
                    deltas.append(a[i]-Y[t])
                else:
                    deltas=[np.array(np.matmul(deltas[0],weights[i])*a[i]*(1-a[i]))]+deltas
            #deltas[0] corresponds to second delta term dletas[1] corresponds to third delta term etc, if numerating 
            #of layers started from 1
            
            d_weights=[]
            for i in range(len(weights)):#calculating d_weight for each weight
                if i == len(arch)-1:
                    d_weights.append(np.matmul(deltas[i].transpose(),a[i])*a[i]*(1-a[i]))
                else:
                    d_weights.append(np.matmul(deltas[i].transpose(),a[i]))
                cap_deltas[i]=cap_deltas[i]+d_weights[i] #accumulate weights updates

        for i in range(len(weights)):#change weights according to acuumulated values
            weights[i]=weights[i]-lr/len(X)*cap_deltas[i]
        cost=sum(1/len(X)*sum_er.reshape(len(Y[0]),))
            
        if previous_cost-cost<0.00000001:
            s.stop=True
        s.cost=cost        
        s.weights=copy.deepcopy(weights)
        
        
    def train(s,X,Y,lr=1,l=0.4):
        """
            Realizes whole training process 
            Input:model object, training set, targets, learning rate, regularization parameter
        """
        k=-1
        while s.stop!=True:
            k+=1
            s.make_one_iteration(X,Y,s.cost,lr,l)
            print("iteration number {0}, cost is {1}".format(k,s.cost))
        print("We stopped cause cost function didn't change enough in last iteration")  

    def predict(s,X):
        """
            Predict values for test set
            Input:model object, test_set
            returns: predictions
        """
        predictions=[]
        weights=s.weights
        for t in range(len(X)):
        #forward propagation
            a=[]
            z=[]
            for i in range(len(s.arch)):
                if i==0:
                    a.append(X[t].reshape(1,s.arch[0]))
                else:
                    z.append(np.matmul(a[i-1],weights[i-1].transpose()))
                    a.append(sig(z[i-1]))
            predictions.append(a[len(s.arch)-1])
        return np.array(predictions).reshape(len(predicitons),)
    
    def find_max_weight(s):
        """
            Finds maximum weight
            Input:model object
            returns:maximum weight
        """
        global flat_weights
        flat_weights=[]
        def get_flat_weights(weights):
            for i in weights:
                if type(i)==list or type(i)==np.ndarray:
                    get_flat_weights(i)
                else:
                    flat_weights.append(abs(i))
        get_flat_weights(s.weights)
        return max(flat_weights)
        

