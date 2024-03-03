import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answers to the questions based on expected behavior:

# What did you see on line 1?
# The output is a random integer between 5 and 20, inclusive of both 5 and 20.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 5, Largest: 20

# What did you see on line 2?
# The output is a random integer from the range 3 to 9, stepping by 2 (i.e., 3, 5, 7, or 9).
# What was the smallest number you could have seen, what was the largest?
# Smallest: 3, Largest: 9
# Could line 2 have produced a 4? No, because the step is 2 starting from 3, so it produces only odd numbers within the range.

# What did you see on line 3?
# The output is a random floating-point number between 2.5 and 5.5.
# What was the smallest number you could have seen, what was the largest?
# Smallest: 2.5, Largest: 5.5

# Code to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)