import random


MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_output.txt"

price = INITIAL_PRICE
number_of_days = 0

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

print(f"Starting price: ${price:,.2f}", file=out_file)


while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    number_of_days += 1
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

out_file.close()

print(f"Simulation ran for {number_of_days} days.", file=out_file)