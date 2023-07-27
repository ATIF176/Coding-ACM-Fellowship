opt = 'yes'
while opt == "yes":
   limiting_number = int(input("Enter a limiting number to find sum: ")) 
   sum_of_integers = (limiting_number * (limiting_number +1)) / 2 # arithmetic series formula
   print("Sum of all smaller integers than given number is:", sum_of_integers)
   opt = input("Enter 'yes' for continue 'q' for quit: ").lower()