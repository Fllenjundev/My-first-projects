import math

def addition(x,y):
  print("Choose your numbers: ")
  while True:
    try:
      x=float(input("1. "))
      y=float(input("2. "))
      print(f"Addition of {x} and {y} is {x+y}")
      break
    except ValueError:
          print("You can't operate with a string or None")
          print("Try again...")
     
def subtraction(x,y):
  while True:
    try:
      print("Choose your numbers: ")
      x=float(input("1. "))
      y=float(input("2. "))
      print(f"Subtraction between {x} and {y} is {x-y}")
      break
    except ValueError:
       print("You can't operate with a string or None")
       print("Try again...")
    
def multi(x,y):
  while True:
    try:
      print("Choose your numbers: ")
      x=float(input("1. "))
      y=float(input("2."))
      print(f"Multiplication between {x} and {y} is {x*y}")
      break
    except ValueError:
          print("You can't operate with a string or None")
          print("Try again...")

def division(x,y):
  while True:
    try:
       print("Choose your numbers: ")
       x=float(input('1. '))
       y=float(input('2. '))
       print("Would you prefer an integer division or leave it as is? ")
       ch = input("Choose int or reg \n").lower().strip()
       if ch=='int':
          int(x,y)
          print(f"Division between {x} and {y} is {x//y}")
          break
       elif ch=='reg':
          print(f"Division between {x} and {y} is {"%.4f" % (x/y)}")
          break
       else:
          print("Choose int or reg. Try again...")
    except ZeroDivisionError:
        print("Can't divide with zero!")
    except ValueError:
          print("You can't operate with a string or None")
          print("Try again...")

def explonen(x,y):
   while True:
        try:
          print("Choose two numbers: ")
          x=int(input("1. "))
          y=int(input("2. "))
          print(f"{x} to the power of {y} is {x**y}")
          break
        except ValueError:
              print("You can't operate with a string or None")
              print("Try again...")

def roots(x,y):
   while True:
     try:
        print("Choose two numbers: ")
        x=int(input("1. "))
        y=int(input("2. "))
        print(f"The square root of {x} and {y} is {"%.2f" % (math.sqrt(x)),"%.2f" % (math.sqrt(y))}")
        break
     except ValueError:
          print("You can't operate with a string or None or 0")
          print("Try again...")

def log(x,y):
   while True:
      try:
       print("Choose two numbers: ")
       x=int(input("1. "))
       y=int(input("2. "))
       print(f"The logarith of {x} and {y} is {"%.2f" % (math.log(x)),"%.2f" % (math.log(y))}")
       break
      except ValueError:
         print("You can't operate with a string or None or 0")
         print("Try again...")
   
    

x,y=0.0,0.0
print("SIMPLE CALCULATOR")
print("Choose between these options: ")
print("1.Addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Explonentiation \n 6.Roots \n 7.Logarithms \n 8.Exit")
while True:
  match int(input("Choose between 1 and 8 \n")):
    case 1: 
      addition(x,y)
      break
    case 2:
      subtraction(x,y)
      break
    case 3:
      multi(x,y)
      break
    case 4:
      division(x,y)
      break
    case 5:
      explonen(x,y)
      break
    case 6:
        roots(x,y)
        break
    case 7:
        log(x,y)
        break
    case 8:
        print("Terminating program...\nGoodbye!")
        break
    case _:
      print("Choose between 1 and 8..Try again!")
