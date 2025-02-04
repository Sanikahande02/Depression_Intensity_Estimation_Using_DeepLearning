import random
import math
import numpy as np


weight=[0.3,0.45,0.12,0.65,0.88,0.83,0.48,0.67,0.89,0.22]
def relu(x):
    return(np.maximum(0, x)) 
   

def getOutputLayer(hiddenlayer,layer):
    outputlayers=[]
    for i in range(layer):
        bias=1
        outputvalue=0.0
        for r in hiddenlayer:
            w=random.choice(weight)
            outputvalue=outputvalue+r*w
            
        outputvalue=outputvalue+bias
        outputlayervalue=relu(outputvalue)    
        outputlayers.append(outputlayervalue)
    
    t1=0.01;
    t2=0.99;
    
    annprobaval=0.5*math.pow(t1-outputlayers[0],2)+0.5*math.pow(t2-outputlayers[1],2);
    return annprobaval
       

def getHiddenLayer(row,layer):
    hiddenlayers=[]
    
    for i in range(layer):
        bias=1
        hiddenvalue=0.0
        
        j=1
        for j in range(len(row)-1):
            if j!=0:
                #print(row[j])
                w=random.choice(weight)
                hiddenvalue=hiddenvalue+row[j]*w
        
        hiddenvalue=hiddenvalue+bias
        hiddenlayervalue=relu(hiddenvalue)
        hiddenlayers.append(hiddenlayervalue)
    
    annprobabilityvalue=getOutputLayer(hiddenlayers,2)
    return annprobabilityvalue


def sort(annprobabilitylist,index):
    annprobabilitylist.sort(key = lambda x: x[index],reverse=True) 
    return annprobabilitylist

def getANNProbabilityList(anninputlist):  
    annprobabilitylist=[]
    annprobvalue=[]
    layer=10
    index=0
    for row in anninputlist:
        temp=[row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],
               row[13],row[14],row[15],row[16],row[17],row[18],row[19]]
        annprobavalue=getHiddenLayer(temp, layer)
        annprobavalue=round(annprobavalue,5)
        row[len(row)-1]=annprobavalue
        index=len(row)-1
        annprobabilitylist.append(row)
        annprobvalue.insert(0, annprobavalue)
        
    annprobabilitylist=sort(annprobabilitylist,index)    
    return annprobabilitylist,annprobvalue

