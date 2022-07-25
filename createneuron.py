import numpy as numpy
import math

def createneuron(inp_for_sys,cnt_MF):
    datapoints=[]
    if cnt_MF % 2:
        sd_cnt=math.floor(cnt_MF/2)
        sd_cnt=3/sd_cnt
        datapoints.append(inp_for_sys)
    else:
        sd_cnt=cnt_MF/2
        sd_cnt=3/sd_cnt
    for i in range(int(sd_cnt),3,int(sd_cnt)):
        minsigma=(inp_for_sys-(i*3))
        plussigma=(inp_for_sys+(i*3))
        numpy.concatenate((datapoints,[minsigma],[plussigma]), axis=0)
    datapoints.sort()
    print(datapoints)
    return datapoints
