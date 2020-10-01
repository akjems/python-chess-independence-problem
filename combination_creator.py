def add_piece_to_board(current_setup, new_piece):
    """Returns a set of tuples, where first is position, and second is avaliable squares
    Combines an existing setup with possible positions of an added piece to create a new board setup.
    To be run in loop with addition of each new piece.
    """


    #print(f'current_setup: {current_setup}')
    #print(f'new_piece: {new_piece}')
    #print(f'current_setup, current_setup: {current_setup}')
    #print(f'new_piece, new_piece: {new_piece}\n')

    updated_setup=set()

    i=0
    print(f'current_setup: \n{current_setup}\n')
    print(f'type(current_setup): {type(current_setup)}')
    print(f'len(current_setup): {len(current_setup)}\n')

    while i < len(current_setup):
        p=0
        while p < len(new_piece):
            # Only continue where posisitons dont overlap
#https://stackoverflow.com/questions/59825/how-to-retrieve-an-element-from-a-set-without-removing-it
            if current_setup.isdisjoint((list(new_piece)[p][0])):
                #print(f"list(new_piece)[p][1]): {len(list(new_piece)[p][1])}")
                if list(current_setup)[i][0].issubset(list(new_piece)[p][1]) & list(new_piece)[p][0].issubset(list(current_setup)[i][1]):

                    first_tuple=list(new_piece)[p][0].union(list(current_setup)[i][0])
                    #print(f'i: {i},p: {p}')
                    second_tuple=list(current_setup)[i][1]&list(new_piece)[p][1]
                    #print(f'{first_tuple}, {second_tuple}\n')

                    updated_setup.add((first_tuple,second_tuple))
                    #print(f'len(updated_setup): {len(updated_setup)} ')
            p+=1
        i+=1
    
    return (frozenset(updated_setup))
