#assignment-A
number=int(input("enter a number: "))
if number %2==0:
    print("Number is even.")
else:
    print("Number is odd.")
print("Thank you")


#assignment-B

total_sum = 0
for number in range(1, 51):
    total_sum += number
print(f"The sum of numbers from 1 to 50 is: {total_sum}")
