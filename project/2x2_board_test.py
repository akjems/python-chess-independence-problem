# 2x2 board test


available_bishop_dict_tuple = {
    (1): frozenset({2,3}),
    (2): frozenset({1,4}),
    (3): frozenset({1,4}),
    4: frozenset({2, 3})
    }
available_knight_dict_tuple = {
    (1): frozenset({2, 3, 4}),
    (2): frozenset({1, 3, 4}),
    (3): frozenset({1, 2, 4}),
    (4): frozenset({1, 2, 3})
    }
combined_dict = {}
for i in available_bishop_dict_tuple.keys():
    for j in available_knight_dict_tuple.keys():
        if (j != i) and (j in available_bishop_dict_tuple.get(i)):
            combined_dict[(j, i)] = available_bishop_dict_tuple.get(j).\
                intersection(available_knight_dict_tuple.get(i))
print(f'combined_dict: {combined_dict}')
combined_dict_2={}
for i in combined_dict.keys():
    for j in available_knight_dict_tuple.keys():
        if (j not in i) and (j in combined_dict.get(i)):
            new_position = (j,)
            new_taken = i+new_position
            combined_dict_2[new_taken] = combined_dict.get(i).\
                intersection(available_knight_dict_tuple.get(j))
print(len(combined_dict_2))
print(combined_dict_2)