#calc the sumation of 3 to 38  39 is exclusive
sumation = 0
for i in range(3,39):
    sumation += (i**2) +1

#print(sumation)

#calc the pi notation of 3 to 14
product = 1
for i in range(3,15):
    product = product*i 

#print(product)

def is_even(num1):
   ans=num1%2
   return ans ==0

    
for i in range(1,101):
   if(is_even(i)):
    print(i,"is even")
   else: 
      print(i,"is odd")

# print(is_even(50))
# print(is_even(51))

