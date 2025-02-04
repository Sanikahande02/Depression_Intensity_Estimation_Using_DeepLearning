import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
class Preprocessing:
    def __init__(self,dataframe):
        self.df=dataframe  
        
    def dataPreprocessing(self):
        print("\n")
        print('Shape of the file')#Number of Rows and Columns
        print('************************************************************************')
        print(self.df.shape)

        print("\n")
        print('Number of Missing Values per Column')
        print('************************************************************************')
        print("\n")
        print(self.df.isnull().sum())
        
                 
        print("\n")
        print('Find Correlation Between Different Attributes')
        print('************************************************************************')
        print("\n")
        
        dataset=self.df.values.tolist()
        print(dataset)
        
        i=1
        for row in dataset:
            row[0]=i
            i+=1
        
              
        preprocesslist=[]
        for row in dataset:
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
                elif strvalue=='Female':
                    temp.append(int(0))
                elif strvalue=='Male':
                    temp.append(int(1))
                elif strvalue=='Never': 
                    temp.append(int(1))
                elif strvalue=='Almost Never': 
                    temp.append(int(2))
                elif strvalue=='Sometime': 
                    temp.append(int(3))
                elif strvalue=='Fairly often': 
                    temp.append(int(4))
                elif strvalue=='Very often': 
                    temp.append(int(5))
               
            preprocesslist.append(temp)  
            
#         df = pd.DataFrame(preprocesslist, columns =['Sr.No','Name Of Student','Age','Gender','Q.1','Q.2','Q.3','Q.4','Q.5','Q.6','Q.7','Q.8','Q.9','Q.10','Q.11','Q.12','Q.13','Q.14','Q.15','Q.16'
# ], dtype = int)    
#         corrmatrix=df.corr(method='pearson')
#         print("The correlation matrix: ")
#         print("\n")
#         print(corrmatrix)
#         plt.subplots()
#         sns.set(rc={'figure.figsize':(15,11)})
#         sns.heatmap(corrmatrix, vmax=0.9, square=True)
#         plt.show()
        
        return preprocesslist    
              
       
        
               
                
       

