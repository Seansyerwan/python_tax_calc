# The main purpose of this file is to not clog the main file, and make it more readable.
# To stay relevant, we will be working off the 1 October 2024 rates of PRSI.


def prsi_rates(prsi_class:chr,income:float) ->float: # TODO: complete function
    match prsi_class:
        case 'a':
            pass
        case '_':
            raise ValueError("Invalid prsi_class")
