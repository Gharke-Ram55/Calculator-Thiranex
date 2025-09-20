def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a,b):
    if b==0:
        return "Error! Division by zero"
    return a/b

def main():
    print("===calculator program===")
    print("select the operator +, -,*, /")
    while True:
       try:
         num1 = float(input("Enter a number1: "))
         operator = input("enter a opeartor: ")
         num2 = float((input("enter number2:")))
         if operator == '+':
            result = add(num1, num2)
            
         elif operator =="-":
            result = sub(num1, num2)
            
         elif operator =='*':
            result = mul(num1, num2)
            
         elif operator =='/':
            result = div(num1, num2)
            
         else:
            print("Invalid operator")
            continue
        
         print(f"{num1}{operator}{num2}={result}")
        
       except  ValueError:
           print("Invalid input! Please enter numeric values.")
           
       again = input("Do you want to perform any operations")
       if again.lower()!='y':
           print("Exiting the program.")
           break
       
if __name__ =="__main__":
    main()
    