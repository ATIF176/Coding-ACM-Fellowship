how_nums = int(input("How many numbers are? "))
total_sum = 0

iteration = 1
for n in range(how_nums):
    numbers = float(input("Enter " + str(iteration) + " number: ")) 
    iteration += 1
    total_sum += numbers

avg = total_sum/how_nums

print("\n<-------------->")
print("Average is:", avg)
print("<-------------->")