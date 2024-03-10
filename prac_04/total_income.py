def main():
    """Display income report for incomes over a given number of months."""
    income_list = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = get_income_input(month)
        income_list.append(income)

    print_income_report(number_of_months, income_list)
def get_income_input(month):
    """Get and return the income input for the specified month using an f-string."""
    return float(input(f"Enter income for month {month}: "))
def print_income_report(months, incomes):
    """Print the income report for the given months and incomes."""
    print("\nIncome Report\n----------------")
    total = 0
    for month in range(1, months + 1):
        income = incomes[month - 1]
        total += income
        print(f"Month {month:2} -   Income: ${income:10.2f}   Total: ${total:10.2f}")


main()