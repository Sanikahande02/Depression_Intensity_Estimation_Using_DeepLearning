import math

class KNN:
    
    def __init__(self, df):
        self.df=df

    #===========================Code to find eucledian distance====================
    def euclidean_distance(self,row1, row2):
        distance=0.0
        for i in range(len(row1)-1):
            
            distance += math.pow(row1[i]-row2[i],2)
            
        return math.sqrt(distance)  
    
    #===========================Code to sort Knn_list+++===========================
    
    def sort(self,knn_list, index):
    
        knn_list.sort(key = lambda x: x[index]) 
        return knn_list     
    
    #===========================Code to find k value===============================
    
    def find_K_Value(self,knn_list):
        
        firstrow=knn_list[0]
        lastrow=knn_list[len(knn_list)-1]
        
        min=firstrow[len(firstrow)-1]
        max=lastrow[len(lastrow)-1]
        
        # print("Min: ",min)
        # print("Max: ",max)
        
        k=max-min
        k=k/2
        k=min+k
        k=round(k,2)
       # print("K Value: ",k)
        return k
    
    
    def getKNNClusters(self,knn_list,k):
        knnclusters=[]
       
        for row in knn_list:
            value=row[len(row)-1]
            if(value<=k):
                knnclusters.append(row)
            
        
        return knnclusters
        
    def knnInit(self):
        
        knn_list=[] 
        index=0
        
        
        for row1 in self.df:
           # print("row1 ",row1)
            sum=0.0
            for row2 in self.df:
              #  print("row2 ",row2)
                if(row1!=row2):
                   
                   temp1=[row1[2],row1[3],row1[4],row1[5],row1[6],row1[7],row1[8],row1[9],row1[10],row1[11],row1[12],row1[13],row1[14],row1[15],row1[16],row1[17],row1[18],row1[19]]
                   temp2=[row2[2],row2[3],row2[4],row2[5],row2[6],row2[7],row2[8],row2[9],row2[10],row2[11],row2[12],row2[13],row2[14],row2[15],row2[16],row2[17],row2[18],row2[19]]
                   sum +=self.euclidean_distance(temp1,temp2)
                                              
            distance=abs(sum/len(self.df)-1)
            distance=round(distance,2)
            row1.insert(len(row1),distance)
            knn_list.append(row1)
            index=len(row1)-1
            #print("index: ",index)
    
        knn_list=self.sort(knn_list,index)
        # k=self.find_K_Value(knn_list)
        # knnclusters=self.getKNNClusters(knn_list,k)
        
        return knn_list
        