#Given tow numbers N and M, find the summation of their last digits.
# Input 
# The first line of the input contains two integers N and M (1 ≤ N, M ≤ 10^18).
# Output
# Output a single integer, the summation of the last digits of N and M.

try:
    Numbers = input("Enter two numbers N and M separated by space: ")
    N, M = map(int, Numbers.split())

    # Calculate the last digits of N and M (when we divide by 10, the remainder is the last digit)

    last_digit_N = N % 10
    last_digit_M = M % 10

    # Calculate the sum of the last digits

    result = last_digit_N + last_digit_M

    # Output the result
    print(result)
except ValueError:
    print("Invalid input. Please enter two integers separated by space.")
