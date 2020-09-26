
# User can run assigned numbers or input own values:


def start_menu():
    user_defined = input("Run assignment numbers, 6x9 board with 2 Kings, 1 Queen, 1 Bishop, 1 Rook and 1 Knight ? (y/n) ")
    if user_defined == 'n':
        # TODO Check input validity 
        M = int(input("How many rows ? (0+) "))
        N = int(input("How many columns ? (0+)"))
        kings = int(input("How many kings? (0+)"))
        queens = int(input("How many queens? (0+)"))
        rooks = int(input("How many rooks? (0+)"))
        bishops = int(input("How many bishops? (0+)"))
        knights = int(input("How many knights? (0+)"))
    else: 
        M = 6
        N = 9
        kings = 2
        queens = 1
        rooks = 1
        bishops = 1
        knights = 1


    parameters = {'row': M, 'columns':N, "Kings": kings, "Queens": queens, "Rooks": rooks, "Bishops": bishops, "Knights": knights}

    #Check for quick wins before running rest of program

    if M*N <= kings+queens+rooks+bishops+knights:
        result = 0
        print(f'More pieces than spaces on board. Result: {result}')
    elif 0 == kings+queens+rooks+bishops+knights:
        result = 0
        print(f'No pieces on board. Result: {result}')
    elif 1 == kings+queens+rooks+bishops+knights:
        result = M*N
        print(f'Only 1 piece on board. Result: {result}')
    else:
        setup = {'M':M, 'N':N, 'kings':kings, 'queens': queens, 'rooks': rooks, 'bishops': bishops, 'knights': knights}
        return (setup)