def add_piece_to_board(current_setup, new_piece):
    """Returns a dictionary, where key is tuple of occupied position and value is available squares
    Combines an existing setup with possible positions of an added piece to create a new board setup.
    To be run in loop with addition of each new piece.
    """

    combined_dict={}

    # {(1, 2): frozenset({3}), (1, 3): frozenset({2}) ...
    for i in current_setup.keys():  # i = (1, 2)

        # For each tuple element
        #print(available_knight_2_dict_tuple.keys())
        for j in new_piece.keys():

            if (j[0] not in i) and (j[0] in current_setup.get(i)):
                new_position = (j)
                new_taken = i+new_position

                combined_dict[new_taken] = current_setup.get(i).intersection(new_piece.get(j))
    


    return(combined_dict)

