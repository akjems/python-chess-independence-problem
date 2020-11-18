# User can run assigned numbers or input own values:

def int_input(msg):
    """Confirm inputs are ints otherwise provide helpful message"""
    while True:
        try:
            number = input(msg)
            number = int(number)
            break
        except ValueError:
            print("Only int values allowed.\n"
                  "An int is a whole number.\n"
                  "152 is an int, 1.24 is not.")
            continue
    return number


def start_menu():
    m = int_input("How many rows ? (0+): ")
    n = int_input("How many columns ? (0+):")
    kings = int_input("How many kings? (0+): ")
    queens = int_input("How many queens? (0+): ")
    rooks = int_input("How many rooks? (0+): ")
    bishops = int_input("How many bishops? (0+): ")
    knights = int_input("How many knights? (0+): ")
    parameters = {
        'M': m, 'N': n,
        "kings": kings,
        "queens": queens,
        "rooks": rooks,
        "bishops": bishops,
        "knights": knights
    }
    return parameters
