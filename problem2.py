# Given three numbers A, B and C, find the minimum and maximum among them.
# Input
# Only one line containing 3 numbers A, B and C ( - 105 ≤ A, B, C ≤ 105).
# Output
# Print the minimum number followed by a single space then print the maximum number.

try:
    Numbers = input() 

    # Calculate the minimum and maximum among A, B and C
    minimum = min(map(int, Numbers.split()))
    maximum = max(map(int, Numbers.split()))

    # Output the result
    print( minimum, maximum)
except ValueError:    
    print("Invalid input. Please enter three integers separated by space.")
