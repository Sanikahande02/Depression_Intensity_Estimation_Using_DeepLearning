def getDecisionTreeResult(dtinputlist):
    dtlist=[]
    for row in dtinputlist:
        sum=0
        for i in range(len(row)-1):
            if i>2:
                sum=sum+row[i]
        #print("sum: ",sum)
        row[len(row)-1]=sum
        dtlist.append(row)
    
    vl=[]
    l=[]
    m=[]
    h=[]
    vh=[]
    
    dtfinalresult=[]
    for row in dtlist:
        value=row[len(row)-1]
        if value<25:
            vl.append(row)
        elif value>=26 and value<=35:
            l.append(row)
        elif value>=36 and value<=50:
            m.append(row)
        elif value>=51 and value<=65:
            h.append(row)
        elif value>=66:
            vh.append(row) 
    dtfinalresult.append(vl)
    dtfinalresult.append(l)
    dtfinalresult.append(m) 
    dtfinalresult.append(h)
    dtfinalresult.append(vh)
       
    return dtfinalresult
