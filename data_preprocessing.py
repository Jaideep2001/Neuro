import numpy as np
import pandas as pd

def data_preprocessing(filename): 
    whole_data=pd.read_excel(filename)
    endeffector_coor=whole_data.drop("Class",axis=1)
    motor=whole_data.Class
    motor=motor.tolist()
    x=round(0.66*len(motor))
    traindata=endeffector_coor[1:x]
    trainout=motor[1:x]
    testdata=endeffector_coor[x:]
    testout=motor[x:]
    return [traindata,trainout,testdata,testout]
            
                        
                        
