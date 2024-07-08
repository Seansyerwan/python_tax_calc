def calcprsi(num: int, bracket: chr)->int:
    """
    This function will check to calculate the user's PRSI rate
    :param num: Total income
    :param bracket: The group the user belongs to
    :return: tax owed.
    """
    pass


def recursive_usc(num:float) -> int:
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

status = "-"

while status not in "1.2.3.4.":

    status = input("What is your relationship status?\n"
                   "1. Single person\n"
                   "2. Lone parent\n"
                   "3. Married couple/civil partners, one income\n"
                   "4. Married couple/civil partners, two incomes ")

    if(status not in "1.2.3.4."):
        print("Error, choice not in the range. Please try again.")

print(f"USC total: €{usc}")


