def add_piece_to_board(current_setup, new_piece):
    """
    Combines an existing setup with possible positions of an added piece to create a new board setup.
    Meant to be run in loop with addition of each new piece.
    """
    set_a_sets=current_setup


    set_b_sets=new_piece

    #print(f'current_setup: {current_setup}')
    #print(f'new_piece: {new_piece}')
    #print(f'current_setup, set_a_sets: {current_setup}')
    #print(f'new_piece, set_b_sets: {new_piece}\n')

    set_c_sets=set()

    i=0
    #print(f'set_a_sets: {type(list(set_a_sets)[0][0])}')

    while i < len(set_a_sets):
        p=0
        while p < len(set_b_sets):
            # Checks if positions overlap
            #if min(set_a_sets[i][0]) in set_b_sets[p][0]:
            check = list(set_a_sets)[i][0]

            if check.issubset((list(set_b_sets)[p][0])):
                None
            else:
               
                if list(set_a_sets)[i][0].issubset(list(set_b_sets)[p][1]) & list(set_b_sets)[p][0].issubset(list(set_a_sets)[i][1]):

                    first_tuple=list(set_b_sets)[p][0].union(list(set_a_sets)[i][0])
                    #print(f'i: {i},p: {p}')
                    second_tuple=list(set_a_sets)[i][1]&list(set_b_sets)[p][1]
                    #print(f'{first_tuple}, {second_tuple}\n')

                    set_c_sets.add((first_tuple,second_tuple))
            p+=1
        i+=1
    
    return (set_c_sets)
