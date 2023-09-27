import art 
print(art.logo)

def add(n1,n2) :
  return n1 + n2

def sub(n1,n2) :
  return n1 - n2

def multi(n1,n2) :
  return n1 * n2

def div(n1,n2) :
  return n1 / n2

function = {
  "+" : add ,
  "-" : sub ,
  "*" : multi ,
  "/" : div ,
 }

compute_again = True 

n1 = int(input("Enter the 1st number :\n"))

while compute_again :

  print("Enter the operation you want to perform :")
  for key in function :
    print(key)
  
  op = input()
  n2 = int(input("Enter the 2nd number :\n"))
  
  operation = function[op]
  
  result = operation(n1,n2)
  
  print(f"The result is : {result} \n")
  print(f" {n1} {op} {n2} = {result} \n")
  
  again = input("Want to continue if yes then type y otherwise type n [y/n] :\n").lower()
  if again == "n" :
    compute_again = False 
    print("Thanks for using our calculator ):")
  n1 =result







