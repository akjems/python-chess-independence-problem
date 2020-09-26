# Use key from dict1 as value in dict2. 
"""
1. i put the king at 3, which leaves 1,5, avaliable
2. Check Knight values at 1, which are 2,4,5,6,7. Key value of king does not match value at knight key 3 therefore allowed
3. Check knight value at 5, which are 1,2,4,6,8. Key value of king does match value at knight key, 5 therefore allowed.
4. Create a new dictionary that includes positions of the two pieces and avaliable fields. 

So the key needs to be a list of positions

If a position is avaliable, the positions of the two pieces are created as the key and the avaliable squares are combined in the value list.

"""

def add_piece_to_board_looped(current_board, new_piece):
    """
    for each current_piece_key:
        search new_piece_values
        if current_piece_key == one of new_piece_values
            updated_dict[[current_piece_key, new_piece_key]]=[current_piece_values-new_piece_values]
            
            ]
    final answer is, after running for each piece, length of updated_dict
    list(current_board.keys())[list(mydict.values()).index(16)]
    """

    # Combine the two loops to produce one dictionary

    # It needs to go both ways, currently only goes one way
    # Check knight threatens king
    for key_search in current_board.keys():
        for key_new_piece in new_piece.keys():
            new_piece_values=new_piece.get(key_new_piece)
            print('')
            print(f'King @ {key_search}')
            print(f'Knight @ {key_new_piece}')
            if key_search in new_piece_values:
                print("Allowed")

            else: 
                print(f'not allowed')

    # Check king threatens knight
    for key_search in new_piece.keys():
        for key_current_board in current_board.keys():
            current_board_values=current_board.get(key_current_board)
            print('')
            print(f'King @ {key_search}')
            print(f'Knight @ {key_current_board}')
            if key_search in current_board_values:
                print("Allowed")

            else: 
                print(f'not allowed')
        #for val in new_piece.values():
        #    print(val.iteritems())
       # if list(new_piece.keys())[list(new_piece.values()).index(key)]:
       #     key in new_piece.values
     #       print(list(new_piece.keys())[list(new_piece.values()).index(key)])
     #   else:
     #       print("not in list")

kings = {1: [3, 7, 8], 2: [4, 8], 3: [1, 5], 4: [2, 6], 5: [3, 7], 6: [4, 8], 7: [1, 5], 8: [1, 2, 6]}
knights = {1: [2, 4, 5, 6, 7], 2: [1, 3, 5, 6, 7, 8], 3: [2, 4, 6, 7, 8], 4: [1, 3, 5, 7, 8], 5: [1, 2, 4, 6, 8], 6: [1, 2, 3, 5, 7], 7: [2, 3, 4, 6, 8], 8: [3, 4, 5, 7]}

mydict = {'george': 16, 'amber': 19}
print(list(mydict.keys())[list(mydict.values()).index(16)])
3 in [1, 2, 3]


#add_piece_to_board_looped(kings,knights)

# Instead of looping it, do it one at a time first.

kings.key() 

list(kings)[0] # prints first key

list(knights.values()) # creates a list of lists with knights values but i loose the key does that matter

data = [['a','b'], ['a','c'], ['b','d']]
search = 'c'
any(e[1] == search for e in data)

search = 1
i=0
while i < len(knights): 
    (e[i] == 1 for e in list(knights.values()))
    i += 1