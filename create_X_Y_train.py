import pandas as pd
import numpy as np
import random as rd
from sklearn.preprocessing import StandardScaler as ss

#create dataset from titanic dataset
def create(Path_to_train, Path_to_targets):
    """
        Creates Train dataset and targets from csv file
        returns:train dataset, targets
    """
    X_train=pd.read_csv(Path_to_train)
    
    Y_train=pd.read_csv(Path_to_targets)
    
    X_train=np.array(X_train)
    Y_train=np.array(Y_train)
    
    s=ss()
    X_train=s.fit_transform(X_train)
    
    X,Y=X_train,Y_train
    return X,Y

