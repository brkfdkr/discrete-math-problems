
def crt(a,b):
    
    #Create Number set
    modcount=b[0]
    for j in range(0,len(b)-2):
        numset=0
        for i in range(b[j+1]):
            numset=a[0]+modcount*i
            
            if(numset%b[j+1]==a[-(len(b)-1-j)]):
                a.insert(0,numset) #First element of an remainders array is now next remainder
                modcount*=b[j+1]
            else:
                continue
    
    return a[0]


import time

start = time.perf_counter() #start value of time
m=2
while(True):
    #Define list of remainders and mods
    a=[]
    b=[]
    #Creating arrays with remainder "0"
    for i in range(m-1):
        a.append(0)
        b.append(i)
    
    X=crt(a,b) #Calling equations
    
    end = time.perf_counter() #end-start= time counter as second
 
    print("Num of equations:{} Answer:{} Time:{}".format(m-1,X,round(end-start,2)))
    m+=1
    

    
