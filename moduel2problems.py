import pandas as pd
#problem 1
#  Write a function introduce(name, age) that prints:
#  My name is <name> and I am <age> years old.
# Call it using positional arguments


def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")


introduce("Rhim", 28)


# Problem 2
# Write a Python generator function called batch_generator. It should take a list of numbers (representing data samples) and a batch_size. The generator should yield one batch at a time as a list.
def batch_generator(data_samples, batch_size):
    for i in range(0, len(data_samples), batch_size):
        yield data_samples[i:i + batch_size]

data = [1, 2, 3, 4, 5, 6, 7, 8]
batch_size = 3
generator = batch_generator(data, batch_size)
print(next(generator))  # Output: [1, 2, 3]
print(next(generator))  # Output: [4, 5, 6] 
print(next(generator))  # Output: [7, 8]     


#problem 3
# Given a list [1,2,3,4], use map() and lambda to create a new list with squares of each number.
number = [1, 2, 3, 4]

df = pd.DataFrame({"number": number})

df["square"] = df["number"].map(lambda x: x ** 2)

print(df)



# Problem 4
#  Write a function power(base, exponent) that returns the result of base raised to exponent. If the exponent is not given, it should calculate the square.


def power(base, exponent=2):
    return base ** exponent

print(power(5))  # Output: 25 (5 squared)


# Problem 5 ( Conceptual Session )
# iven a list [1,2,3,4,5,6], use filter() to select even numbers and map() with lambda to square them.
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squared_even_numbers = list(map(lambda x: x ** 2, even_numbers))

print(squared_even_numbers)