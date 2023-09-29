:numbers = []

num_values = int(input("How many numbers do you want to enter? "))

for i in range(num_values):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)

if len(numbers) > 0:
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average}")
else:
    print("No numbers were entered. Cannot calculate the average.")
