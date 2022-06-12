
#Create array for [n]
from numpy import i0


narray=[]

def permute(n,perm):
    if (len(n)==0):
        #print(perm, end = "  ")
        narray.append(perm)
        return

    for i in range(len(n)):
        c = n[i]
        p1=n[0:i]
        p2=n[i+1:]
        newperm=p1+p2
        permute(newperm,perm+c)

answer = ""
#Input'u kümeye dönüştürmek
n = int(input("Enter the [n] value : "))
s1=[]
x=[]

for i in range(1,n+1):
    s1.append(str(i))
s=''.join(s1)

permute(s,answer)
counter2=0
for i in narray:
    counter=0
    
    for j in range(n):
       ## print("s={} i={} s[{}]={} i[{}]={}".format(s,i,j,s[j],j,i[j]))
        if(s[j]==i[j]):
            counter+=1
        else:
            continue
        
    if(counter==0):
        print(i, end=" ")
        counter2+=1
        continue
    else:
        continue
print("\nNumber of derangements: {}".format(counter2))
