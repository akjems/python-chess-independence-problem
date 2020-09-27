def add_piece_to_board(current_setup, new_piece):
    """
    Combines an existing setup with possible positions of an added piece to create a new board setup.
    Meant to be run in loop with addition of each new piece.
    """
    new_setup=[]

    print(f'current_setup: {current_setup}')
    print(f'new_piece: {new_piece}')
    new_setup=current_setup+new_piece

    #print(f'new_setup: {new_setup}')
    return (new_setup)

list_a_sets=[({1},{2,3}),({2},{1,3}),({3},{1,4})]
list_b_sets=[({1},{3,4}),({2},{3,4})]
list_c_sets=[]
#print(f'list_a_sets[0][0]: {list_a_sets[0][0]}')
#print(f'list_b_sets[0][0]: {list_b_sets[0][0]}')

i=0

while i < len(list_a_sets):
    p=0
    while p < len(list_b_sets):
        print(f'i: {i}, p: {p}')
        if min(list_a_sets[i][0]) in list_b_sets[p][0]:
            print(f'Pieces cannot share position')
            print(f'list_a_sets[i][0]: {list_a_sets[i][0]}')
            print(f'list_b_sets[p][0]: {list_b_sets[p][0]}\n')
    
        else:
            print(f'list_a_sets[i][0]: {list_a_sets[i][0]}')
            print(f'list_b_sets[p][0]: {list_b_sets[p][0]}')

            first_tuple=list_a_sets[i][0]|list_b_sets[p][0]
            print(f'first_tuple: {first_tuple}')

            second_tuple=list_a_sets[i][1]&list_b_sets[p][1]
            print(f'second_tuple: {second_tuple}')

            list_c_sets.append((first_tuple,second_tuple))
            print(f'list_c_set:{list_c_sets}\n')
        p+=1
    i+=1
# result ab=[({1,2},{3}),({3,1},{4}),{3,2},{4})]
i =0
p=0
"""
print(f'list_a_sets: {list_a_sets[1]}')
print(f'Length of a: {len(list_a_sets)}')
while i < len(list_a_sets):
    while p < len(list_b_sets):
        print(f'b_sets: {list_b_sets[p]}')
        print(f'Unpack tuple: {[x for x,_ in list_a_sets]}')

        p +=1

    print(list_a_sets[i])
    i +=1
"""

list_c_sets = []