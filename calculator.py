
calculate = True
while True:
    
   print("1 = Addition")
   print("2 = Subtraction")
   print("3 = Division")
   print("4 = Multiplication")
   print("5 = Modulus")

   user_input = input("Select operation: ")
   num1 = int(input("First Number: "))
   num2 = int(input("Second Number: "))

   if user_input == "Addition":
      print(num1 + num2)
   elif user_input == "Subtraction":
      print(num1 - num2)    
   elif user_input == "Division":
      print(num1 / num2)    
   elif user_input == "Multiplication":
      print(num1 * num2)
   elif user_input == "Modulus":
      print(num1 % num2)     
   else:
      print("Invalid Operation!")     

   option =input("Would you like to reuse our calculator? ") 
   if option == "Yes":
    pass
   if option == "No":   
    break

   print("Thanks for using our calculator! Rate us.")