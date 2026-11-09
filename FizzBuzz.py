'''A simple program where we print the numbers from 1 to 100
We check if the number can be divided by 3 and 5 and depending on the result
it either is a Fizz or Fuzz number respectively
And if it is divided by 3 and 5 then it is a FizzFuzz number
else we print them as Regular numbers'''

print("Welcome to FizzBuzz \n")
fizzbuzzNums=[]
regularNums=[]
fizz=[]
fuzz=[]
for i in range(0,101):
    if i % 3 == 0:
       fizz.append(i)
    elif i % 5 == 0:
        fuzz.append(i)
    else:
        regularNums.append(i)
    
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzzNums.append(i)
    
print("The FIZZ numbers are:")
print(fizz,'\n')

print("The FUZZ numbers are:")
print(fuzz,'\n')

print("The FIZZBUZZ numbers are: ")
print(fizzbuzzNums,'\n')

print("The REGULAR numbers are:")
print(regularNums,'\n')