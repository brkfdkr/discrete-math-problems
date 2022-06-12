
a=input("Please enter your array: ")
k=int(input("Please enter the r value: "))
##Create array for [n]
narray=list(a)
n=len(narray)
#Create binary values
subset=[]
for t in range(2**(n),2**(n+1)):
    barray=list(bin(t))
    a=[]
    
    for i in range(n):
        
        if barray[3+i]=='1':
            
            a.append(str(narray[i]))
            
        else:
            continue
    
    if len(a)==k:
        if ''.join(a) not in subset:
            subset.append(''.join(a))
           
    else:
        continue
print("Subsets(Combinations): ")
print(subset)
print("\n")

def permute(n,perm):
    if (len(n)==0):
        if perm not in perm_array:
            perm_array.append(perm)

        

    for i in range(len(n)):
        c = n[i]
        p1=n[0:i]
        p2=n[i+1:]
        newperm=p1+p2
        permute(newperm,perm+c)

answer = ""
print("Permutations : ")

perm_array=[]
for s in subset:
    permute(s, answer)
print(perm_array)
