def add_piece_to_board(current_setup, new_piece):
    """Returns a dictionary, where key is tuple of occupied position and value is available squares
    Combines an existing setup with possible positions of an added piece to create a new board setup.
    To be run in loop with addition of each new piece.
    """

    combined_dict = {}
    for i in current_setup.keys():  # i = (1,3)...
        for j in new_piece.keys(): # j= (1,)
            if (j[0] not in i) and (j[0] in current_setup.get(i)):
                # There are squares where new piece is not threatened. I need to check if new piece threatens existing.
                if set(i).issubset(set(new_piece.get(j))):
                    new_position = (j)
                    new_taken = i+new_position
                    combined_dict[new_taken] = \
                        current_setup.get(i).intersection(new_piece.get(j))
    return combined_dict
