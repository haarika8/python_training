
def switch(): 

   a = int(input("Enter num1 value: "))
   b = int(input("Enter num2 value: "))
   print("Press 1 for Addittion \nPress 2 for Subtraction \nPress 3 for Multiplication \nPress 4 for Division \nPress 5 for Average")
   option = int(input("Enter your option: "))

   if option == 1:
    result = a+b
    print("Addition: ", result)
  
   elif option == 2:
     result = a-b
     print("Subtraction: ", result)
   elif option == 3:
     result = a/b
     print("Division: ", result)
   elif option == 4:
     result = a*b
     print("Multiplication: ", result)
   elif option == 5:
         x = int(input("Enter first value: "))
         y  = int(input("Enter second value: "))
         result = ((a+b+x+y)/4)   
         print("Average: ", result)
   else:
       print("invalid option")

switch()