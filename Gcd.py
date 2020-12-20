#function to find gcd of 2 numbers
#Euclidean algorithm
def gcd(a,b):
    if(b==0):                   #once the second number becomes zero then 'a' is the gcd
        return a
    else:
        return gcd(b,a%b)       #if not then we still need to swap 'b' to 1st place
                                #and in 'b' place 'a%b'


#input of 2 numbers 
a=int(input())
b=int(input())

print(gcd(a,b))
