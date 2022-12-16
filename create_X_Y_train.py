import pandas as pd
import numpy as np
import random as rd
from sklearn.preprocessing import StandardScaler as ss

#create dataset from titanic dataset
def create():
    """
        Creates Train dataset and targets from csv file
        returns:train dataset, targets
    """
    data=pd.read_csv("train.csv")[["Survived","Pclass","Sex","Age","Fare","SibSp"]]
    data=data.fillna(value={"Age":np.mean(data["Age"])})
    data.loc[data.Sex=="male","Sex"]=0
    data.loc[data.Sex=="female","Sex"]=1

    X_train=data[["Pclass","Sex","Age","Fare","SibSp"]]
    Y_train=data[["Survived"]]
    
    X_train=np.array(X_train)
    Y_train=np.array(Y_train)
    
    s=ss()
    X_train=s.fit_transform(X_train)
    
    X,Y=X_train,Y_train
    return X,Y

