#Given N numbers. Count how many of  these values are eve, odd, positive and negative.
# Input
# The first contains one number N (1 ≤ N ≤ 10^3) number of values.
#Second line contains N numbers ( - 105 ≤ A[i] ≤ 105).
# Output
# Print four lines with the following format:

# First Line: "Even: X", where X is the number of even numbers in the given input.

# Second Line: "Odd: X", where X is the number of odd numbers in the given input.

# Third Line: "Positive: X", where X is the number of positive numbers in the given input.

# Fourth Line: "Negative: X", where X is the number of negative numbers in the given input.

try:
    N = int(input())
    numbers = list(map(int, input().split()))

    # Count the number of even, odd, positive and negative numbers
    even_count = sum(1 for num in numbers if num % 2 == 0)
    odd_count = sum(1 for num in numbers if num % 2 == 1)
    positive_count = sum(1 for num in numbers if num > 0)
    negative_count = sum(1 for num in numbers if num < 0)

    # Output the result
    print(f"Even: {even_count}")
    print(f"Odd: {odd_count}")
    print(f"Positive: {positive_count}")
    print(f"Negative: {negative_count}")
except ValueError:
    print("Invalid input. Please enter a number.")