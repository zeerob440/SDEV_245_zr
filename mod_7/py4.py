# Simple Python program to calculate the sum of a set of numbers supplied by the user
# refactored total to start with 0, to remove off-by-one error. uncertain if that was intended. 
total: int = int(0)
num_count: int = int(1)
num: float = float(1.0)

num_count = int(input("How many numbers do you want to add? "))

for number in range(num_count):
    num: float = float(input("Enter number {}: ".format(number + 1)))
    
    total += num

print("The sum of the numbers you entered is:", total)