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


print(round(recursive_usc(100000), 2))

