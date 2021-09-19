# coding: utf-8
import csv
from pathlib import Path

##A few functions are defined here to aid in ease of presentation of numbers in string output.


#This function takes a money amount parameter and rounds it to the penny, and also prints zeros for the pennies place if there are no pennies or an end zero if there are only dimes, and adds a leading dollar sign. The output is returned as a string.

def penny_format(unformatted_amount):
    penny_rounded_format = "${:.2f}".format(round(unformatted_amount, 2))
    return penny_rounded_format

#this function takes a plain decimal format and converts it to a string in percent format, multiplied by a hundred with a percent sign. It removes trailing zeros after a decimal.

def percent_format(decimal_format):
    percent = decimal_format * 100
    if (percent * 100) % 1 == 0:
        percent = int(percent)
    percent_formatted = str(percent) + "%"
    return percent_formatted


"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""

print("Part 1: Automate the Calculations.\n")

loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
total_number_of_loans = len(loan_costs)
print(f"There are {total_number_of_loans} loans.")


# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
loan_amount_total = sum(loan_costs)
print(f"There total amount of the loans is {penny_format(loan_amount_total)}.")

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
average_loan_price = loan_amount_total / total_number_of_loans
print(f"The average loan price is {penny_format(average_loan_price)}.\n")

#This code prints the previous calculations with descriptive messages and formats it to look like a normal accounting equation.
print(f"The sum of the {total_number_of_loans} loans:\n")

#code to add spaces at the beginning so the right side lines up and a plus sign appears before the bottom horizontal line. I should make a general function for this.
for loan in loan_costs[:-1]: 
    print("  " + " "*((len(penny_format(loan_amount_total)))-len(penny_format(loan))) + penny_format(loan))
print("+ " + " "*((len(penny_format(loan_amount_total)))-len(penny_format(loan_costs[-1]))) + penny_format(loan_costs[-1]))

print("  " + "-" * len(penny_format(loan_amount_total)))
print("  " + penny_format(loan_amount_total))

print(f"\nThe total loan amount of {penny_format(loan_amount_total)} divided by {total_number_of_loans} loans equals an average loan price of {penny_format(average_loan_price)}.\n")




"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

print("Part 2: Analyze Loan Data.\n")

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.

future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value of the loan is {penny_format(future_value)} when the loan matures {remaining_months} from now.")


# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

discount_rate = .2
present_value = future_value / (1+discount_rate/12)**remaining_months

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

if loan["loan_price"] <= present_value:
    print(f"This loan is worth at least the cost to buy it if we assume we will be repaid. We are lending " + penny_format(loan["loan_price"]) + f" with an expectation that the present value of the future repayment with a discount rate of " + percent_format(discount_rate) + f" is {penny_format(present_value)}.\n")
else:
    print(f"This loan is not worth the price of " + penny_format(loan["loan_price"]) + f" because even if we do get repaid the present value of the future payment at a discount rate of " + percent_format(discount_rate) + " is {penny_format(present_value)}.\n")


"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

print("Part 3: Perform Financial Calculations.\n")

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1+discount_rate/12)**remaining_months
    return present_value

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.

annual_discount_rate = .2

present_value = calculate_present_value(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

print(f"The present value of the loan of " + penny_format(new_loan["loan_price"]) +" which matures in " + str(new_loan["remaining_months"]) + f" months is: {penny_format(present_value)}\n")



"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than 500
    b. If the loan_price is less than 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

print("Part 4: Conditionally filter lists of loans.\n")

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# @TODO: Print the `inexpensive_loans` list
print("The following loans are priced at under $500.")
loan_number = 1
for loan in inexpensive_loans:
    if loan["repayment_interval"] == "bullet":
        print(f"{loan_number}. A loan for " + penny_format(loan["loan_price"]) + " maturing in " + str(loan["remaining_months"]) + " months with a future value of " + penny_format(loan["future_value"]) + " to be paid in full at maturity.")
    elif loan["repayment_interval"] == "monthly":
        print(f"{loan_number}. A loan for " + penny_format(loan["loan_price"]) + " maturing in " + str(loan["remaining_months"]) + " months with a future value of " + penny_format(loan["future_value"]) + " to be paid monthly.")
    loan_number+=1

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
