

def fac(num):
    if num == 1:
        return num
    else:
        return num * fac(num-1)

num=int(input("enter a number "))

if num < 0 :
    print("cannot be negative")
else:
    print("factorial of ", num, "is ", fac(num))




def upperlower(string): 
  
    upper = 0
    lower = 0
  
    for i in range(len(string)): 
          
        # For lower letters 
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122): 
            lower += 1
  
        # For upper letters 
        elif (ord(string[i]) >= 65 and
              ord(string[i]) <= 90): 
            upper += 1

    print('Lower case characters = %s' %lower, 
          'Upper case characters = %s' %upper) 
  
# Driver Code 
string = 'The BROWN fox Jumps Over the Lazy DOG'
upperlower(string) 
# question 3
list1 =[23,2,3,55,444]
for numberss in list1:
    if numberss %2==0:
        print("even numbers", numberss)

# question 4 
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "the brown fox"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string is : ",end="") 
print (reverse(s)) 


num = int(input("Enter a number: "))  
  
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")  
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number")  


