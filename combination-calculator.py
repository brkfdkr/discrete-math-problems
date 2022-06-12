
n=int(input("Please enter the [n] value: "))
#Create array for [n]
narray=[]

for i in range(1,n+1):
    narray.append(i)

#Create binary values and new array for values
for t in range(2**(n),2**(n+1)):
    barray=list(bin(t))
    a=[]
    for i in range(n):
        
        if barray[3+i]=='1':
            
            a.append(str(narray[i]))
            
        else:
            continue
    print(''.join(a))#combine(join) the values of new array

print("\n")
