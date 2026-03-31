# Given a number N. Print the digits of that number from right to left separated by space.

# Input
# First line contains a number T (1 ≤ T ≤ 10) number of test cases.

# Next T lines will contain a number N (0 ≤ N ≤ 109)

# Output
# For each test case print a single line contains the digits of the number separated by space.

lengthInput = int(input())
arr = []
for i in range(lengthInput):
    inputNumber = int(input())
    arr.append(inputNumber)

for number in arr:
    result = " ".join(str(number)[::-1])
    print(result)
    


 