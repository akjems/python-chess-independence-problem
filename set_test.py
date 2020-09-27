
set_a_sets=[({1}, {2, 3, 4, 6}), ({2}, {1, 3, 5}), ({3}, {1, 2, 4, 6}), ({4}, {1, 3, 5, 6}), ({5}, {2, 4, 6}), ({6}, {1, 3, 4, 5})]
set_b_sets=[({1}, {2, 3, 4, 5}), ({2}, {1, 3, 4, 5, 6}), ({3}, {1, 2, 5, 6}), ({4}, {1, 2, 5, 6}), ({5}, {1, 2, 3, 4, 6}), ({6}, {2, 3, 4, 5})]

#set_a_sets=[({1},{2,3}),({2},{1,3}),({3},{1,4})]
#set_b_sets=[({1},{3,4}),({2},{3,4})]


set_c_sets=set()

#print(f'set_a_sets[0][0]: {set_a_sets[0][0]}')
#print(f'set_b_sets[0][0]: {set_b_sets[0][0]}')

i=0

while i < len(set_a_sets):
    p=0
    while p < len(set_b_sets):
        if min(set_a_sets[i][0]) in set_b_sets[p][0]:

            print(f'')
        else:

            if set_a_sets[i][0].issubset(set_b_sets[p][1]) & set_b_sets[p][0].issubset(set_a_sets[i][1]) :

                first_tuple=set_b_sets[p][0].union(set_a_sets[i][0])
                print(f'i: {i},p: {p}')
                second_tuple=set_a_sets[i][1]&set_b_sets[p][1]
                print(f'{first_tuple}, {second_tuple}\n')

                set_c_sets.add((frozenset(first_tuple),frozenset(second_tuple)))
            #else:
                #failed_tuple=set_a_sets[i][0]|set_b_sets[p][0]
                #print(f'first_faied_tuple: {first_failed_tuple}')

                #second_failed_tuple=set_a_sets[i][1]&set_b_sets[p][1]
                #print(f'second_failed_tuple: {second_failed_tuple}\n')
                #print(f'')
        p+=1
    i+=1
# result ab=[({1,2},{3}),({3,1},{4}),{3,2},{4})]



print(f'set_c_sets: {len(set_c_sets)}\n')


