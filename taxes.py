import csv


def calcpaye(num:float, cutoff:float) -> float:
    """
    Takes in number, calculating the total PAYE amount to be paid
    :param num: The num is the amount that is to be taxed
    :param cutoff: The cutoff for the 20% tax limit
    :return: The total tax to be paid.
    """
    if num <= cutoff:
        return num*.2
    else:
        return ((num-cutoff)*.4) + cutoff*.2



def recursive_usc(num:float) -> float:
    """
    Getting the Universal Social Charge total for the user.
    :param num: The amount remaining to be charged
    :param percent: The percentage for the next bit to be charged at
    :return: The amount owed, returned recursively.
    """

    num2 = 0.00 # declare just to store temporary values
    if num <= 12012.00:
        return num*.005
    elif num-12012.00 < 13748.01:
        num2 = num-12012.00
        return num2*.02 + recursive_usc(num-num2)
    elif num-25760 < 44284.01:
        num2 = num-25760.00
        return (num2*.04) + recursive_usc(num-num2)
    else:
        num2 = num - 70044.00
        return num2*.08 + recursive_usc(num-num2)


income = float(input("How much do you earn per annum? "))

usc = (round(recursive_usc(income), 2))
paye = 0;

status = "-"
# we continuously check the status of the user, so that we can add this to the data.
while status not in "1.2.3.4.":

    status = input("What best describes your status?\n"
                   "1. Single person\n"
                   "2. Lone parent\n"
                   "3. Married couple/civil partners, one income\n"
                   "4. Married couple/civil partners, two incomes ")

    if status not in "1.2.3.4.":
        print("Error, choice not in the range. Please try again.")

# accounting for any inputs including a .
status = status[0]
print(status)

# the match status statement will connect us to the correct bracket. Thank you, python ver 3.10
match status:
    case "1":
        paye = calcpaye(income,42000.0)
    case "2":
        paye = calcpaye(income, 46000.0)
    case "3":
        paye = calcpaye(income, 51000.0)
    case "4":
        second_income = float(input("How much does your partner earn? "))
        paye = calcpaye(income, 51000.0) + calcpaye(second_income, 33000.0)
        usc += recursive_usc(second_income)
        income += second_income
    case _:
        raise ValueError("Invalid status")

tax_credits = float(input("Please input the tax credits you are owed: "))

# can't have negative tax_credits.
if tax_credits < 0.0:
    tax_credits = 0

total_tax = usc+paye
net_tax = total_tax-tax_credits
if net_tax < 0.0:
    net_tax = 0.0 # we can't get negative tax... unless you did it wrong. we don't want to be wrong.

net_pay = income - net_tax

print(f"Gross pay (before tax): €{income}")
print(f"USC total: €{usc}")
print(f"PAYE total: €{paye}")
print(f"Gross tax (before tax credit): €{usc + paye}")
print(f"Tax credits: €{tax_credits}")
print(f"Net tax: €{usc+paye - tax_credits}")
print(f"Net pay: €{round(income - net_tax, 2)}")


# we turn the data above to a dict.
tax_dict = {"Total Income" : f"€{income}",
            "USC" : f"€{usc}",
            "PAYE": f"€{paye}",
            "Gross Tax": f"€{total_tax}",
            "Tax Credits": f"€{tax_credits}",
            "Net Tax": f"€{net_tax}",
            "Net Pay": f"€{round(net_pay, 2)}"}

filename = "tax_calculation.csv"

with open(filename, 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    for key, value in tax_dict.items():
        writer.writerow([key, value])


