# The main purpose of this file is to not clog the main file, and make it more readable.
# To stay relevant, we will be working off the 1 October 2024 rates of PRSI.


def prsi_rates(prsi_class: chr, income: float) -> float: # TODO: complete function
    match prsi_class:
        case 'a':
            return (income - (352.0*52)) *.041 if income > (352.0*52) else 0.0
        case 'b':
            if income <= (352.0*52): return 0.0
        case 's':
            return income*.041
        case '_':
            return 0.0


