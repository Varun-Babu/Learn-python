#EUCLIDS ALGORITHM

def Gcd(a,b):
    while(b != 0):
        r = a % b
        if r == 0:     #while loop will run infinite since b never becomes 0
            #print("bug") 
            return b
        else:
            a = b
            b = r 

def gcd(a,b):     #different approach same principles
    while(b != 0):
        t = a
        a = b
        b = t % b #b becomes 0 breaking the loop
    return a                    
           
print(Gcd(20,8))  #4
print(Gcd(96,60)) #12       
print(Gcd(6,3))   #3  


print(gcd(20,8))  #4
print(gcd(96,60)) #12       
print(gcd(6,3))   #3     
