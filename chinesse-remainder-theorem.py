#Introduction
print("*****Please enter your modular equations(ENTER 0 0 for answer)****** ")
#Define list of remainders and mods
a=[]
b=[]
#Get mod input from user
a1,b1=1,1
while(int(a1+b1)!=0):

    a1, b1 = input("Enter a mod b as a b: ").split()
    a.append(int(a1))
    b.append(int(b1))


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
                break
            else:
                continue

        
        
        

    print(f"X={a[0]}")

crt(a,b)
