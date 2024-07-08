# The main purpose of this file is to not clog the main file, and make it more readable.
# To stay relevant, we will be working off the 1 October 2024 rates of PRSI.


def prsi_rates(prsi_class: chr, income: float) -> float:
    match prsi_class:
        case 'a':
            return income * .041 if income > (352.0 * 52) else 0.0
        case 'b', 'c', 'd':
            if income < 352.01 * 52:
                return 0.0
            elif income < 1443.01 * 52:
                return income * .009
            else:
                return (1443.0 * 52) * .009 + (income - (1443.0 * 52) * .04)
        case 'e':
            return income * .0343 if income > (352 * 52) else 0.0
        case 'h':
            if income < 352.01 * 52:
                return income * 0.001
            elif income < 424.01:
                return (income * .04) - (12 * 52)
            else:
                return income * .04
        case 'k':
            return income * .041 if income > 100 * 52 else 0.0
        case 'p':
            return (income - 2500) * .041 if income > 2500 else 0.0
        case 's':
            return income * .041
        case 'j':
            return income * .001
        case 'm':
            return 0.0
        case '_':
            raise ValueError("Invalid class.")