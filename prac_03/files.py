user_name = input("What is your name? ")
with open("name.txt", "w") as name_file:
    name_file.write(user_name)

with open("name.txt", "r") as name_file:
    name = name_file.read().strip()
print(f"Your name is {name}")

with open("numbers.txt", "r") as numbers_file:
    first_number = int(numbers_file.readline().strip())
    second_number = int(numbers_file.readline().strip())
print(f"The sum of the first two numbers is: {first_number + second_number}")

total = 0
with open("numbers.txt", "r") as numbers_file:
    for line in numbers_file:
        total += int(line.strip())
print(f"The total of all numbers is: {total}")