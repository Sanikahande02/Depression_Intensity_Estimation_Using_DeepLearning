import pandas as pd
import preprocessing
import knn
import ann
import decisiontree
import matplotlib.pyplot as plt
import numpy as np


# def getEmailID(filepath,name):
#     df=pd.read_excel(filepath)
#     dataset=df.values.tolist()
#     eid=""
#     for row in dataset:
#         uname=row[1]
#         email=row[20]
#        # print("RRR ",row)
       
#         # print('EEE ',email)
#         if(name==uname):
#           #  print("uuu ",name," : ",uname," : ",email," : ",len(name)," : ",len(uname))
#             eid=email
#             break
   
#     return eid 
    
    

def initProcess(filepath):
    
    #*******************Code to Preprocess Dataset***************************************
    df=pd.read_excel(filepath)
    
    print(df.head())
    
    
    pre=preprocessing.Preprocessing(df)
    preprocessdataset=pre.dataPreprocessing()
    #print(preprocessdataset)
    
    
    #*******************Code for KNN***************************************
    print("\n")
    print('Dataset After KNN Clustering')
    print('************************************************************************')
    print("\n")
    #dataset=preprocessdataset.values.tolist()
    kn=knn.KNN(preprocessdataset)
    knnlist=kn.knnInit()
    for row in knnlist:
            print(row)
            
    
    print("\n")
    print("****************************ANN Probability List**************************")
    print("\n")   
        
        
    
    annprobilitylist,annprobvalue=ann.getANNProbabilityList(knnlist) 
    
    for row in annprobilitylist:
        print(row)  
    
    print("\n")
    print("****************************Decision Tree List**************************")
    print("\n")   
    dtinputlist=[]
    index= int (len(annprobilitylist)*90/100)
    for i in range(index):
        row=annprobilitylist[i]
        dtinputlist.append(row) 
        
        
    
    decisiontreelist=decisiontree.getDecisionTreeResult(dtinputlist) 
    
    for row in decisiontreelist:
        for r in row:
            print(r)        
        print("\n")    
    
    print("\n")
    print("****************************Final Result**************************")
    
    finalresult=[]
    for row1 in decisiontreelist:
        temp1=[]
        for row in row1:        
            temp=[]
            k=len(row)
            for i in range(k):
                strvalue=row[i]
                if type(strvalue) == str:
                    strvalue=strvalue.strip()
                if i==0:
                    temp.append(row[0])
                elif i==1:
                    temp.append(row[1])
                elif i==2:
                    temp.append(row[2])
                elif i==3 and strvalue==0:
                    temp.append("Female")
                elif i==3 and strvalue==1:
                    temp.append("Male")
               
                if i>3:
                    if strvalue==1:
                        temp.append("Never")
                    elif strvalue==2:
                        temp.append("Almost Never")
                    elif strvalue==3:
                        temp.append("Sometime")
                    elif strvalue==4:
                        temp.append("Fairly often")
                    elif strvalue==5:
                        temp.append("Very often")    
            temp1.append(temp)            
        finalresult.append(temp1)
    
    k=0
    for row in finalresult:
        if k==0:
            print("\n")
            print("Students With "+"Very Low Mental Stress")
            print("\n")
        elif k==1:
            print("\n")
            print("Students With "+"Low Mental Stress")
            print("\n")              
        elif k==2:
            print("\n")
            print("Students With "+"Medium Mental Stress")
            print("\n")           
        elif k==3:
            print("\n")
            print("Students With "+"High Mental Stress")
            print("\n")          
        elif k==4:
            print("\n")
            print("Students With "+"Very High Mental Stress")   
            print("\n")
        k+=1
        for r in row:
            print(r)         
            
       
        
    vlsname=[]
    lsname=[]
    msname=[]
    hsname=[]
    vhsname=[]
    i=0
  
    for row in finalresult:
        for r in row:
            if i==0:
                vlsname.append(r[1]) 
            if i==1:
                lsname.append(r[1])    
            if i==2:
                msname.append(r[1])
            if i==3:
                hsname.append(r[1]) 
               # hemail.append(r[20])
               
              #  heid= getEmailID(filepath,r[1])
          #      print("HIGH ",r[1]," : ",heid)
                subject1="Regarding High Stress Level"
                body1="Dear "+r[1]+"\n "+ " Your are Predicted with High Stress Level Based on the Answers for the Asked Questions."
                #EMAILSender.sendEmail(heid, subject1, body1)
            if i==4:
                eid=""
                vhsname.append(r[1]) 
              #  vheid=getEmailID(filepath,r[1])
               # vhemail.append(r[20])
             #   print("VERY HIGH ",r[1]," : ",vheid)
                subject2="Regarding VERY High Stress Level"
                body2="Dear "+r[1]+"\n "+ " Your are Predicted with VERY High Stress Level Based on the Answers for the Asked Questions."
                #EMAILSender.sendEmail(vheid, subject2, body2)
        i+=1
    #print(vlsname) 
    vlresult = '\n'.join(vlsname)
    lresult = '\n'.join(lsname)
    mresult = '\n'.join(msname)
    hresult = '\n'.join(hsname)
    vhresult = '\n'.join(vhsname)
    
    ######################Code For Graph#######################################
    y = np.array([len(vlsname), len(lsname), len(msname), len(hsname),len(vhsname)])
    mylabels = ["Very Low", "Low", "Medium", "High","Very High"]

    fig, ax = plt.subplots(figsize=(16,8))
    plt.title("Percentage of Student with Depression Level in Given Dataset")
    plt.pie(y, labels = mylabels)
    plt.show() 
    
    return vlresult,lresult,mresult,hresult,vhresult