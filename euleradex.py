import numpy as np
from voltage.py import Voltage
from current.py import AdCurrent


def EulerAdEx(I):
    
    dt=.025;
    s=0
    x=[]
    while s<=300 :
        x.append(s)
        s=s+0.25
    V=[]
    w=[]
    VV=[]
    spiketime=np.zeros((len(x),),dtype=int);
    mfspike=[];
    Vr=-58;
    b=265;
    el=-70;
    V.append(-60);
    w.append(V[0]-el);
    sp_cnt=1;
    for i in range (0,len(x)):
        V.append(V[i]+dt*(Voltage(V[i],w[i],I));
        w.append(w[i]+dt*(AdCurrent(V[i],w[i]));
        if V[i+1] > 0:
            VV.append(0);
            V.append(Vr);
            w.append(w[i+1]+b);
            spiketime.append(1);
            mfspike[sp_cnt]=t;
            #spikecount would be sp_cnt-1
            sp_cnt=sp_cnt+1;
        else :
            VV.append(V[i+1]);
    return (mfspike)
    
    
