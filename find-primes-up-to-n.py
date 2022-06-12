#Creating bounded array
list=[]
up=int(input("Find prime numbers up to: "))

for i in range(2,up+1):
    list.append(i)


j=0
numtrans=0 #Number of transitions
while(j<len(list)):
    for i in range(2,int(up+1/list[j])):
        numtrans+=1
        try:
            list.remove(list[j]*i)
        except ValueError:
            pass
    j+=1
    

print("Prime Numbers up to",up,":",list)
print("Number of Transitions:",numtrans)
