# 2x2 board test
#avaliable_bishop_dict = {{1}:{2,3},{2}:{3,4},{3}:{1,4},{4}:{2,3}}
#avaliable_knight_dict = {{1}:{2,3,4},{2}:{1,3,4},{3}:{1,2,4},{4}:{1,2,3}}

# Lists are mutable and therefore cannot be used as dict keys

avaliable_bishop_dict_tuple = {
    (1):frozenset({2,3}),
    (2):frozenset({1,4}),
    (3):frozenset({1,4}),
    (4):frozenset({2,3})
    }

avaliable_knight_dict_tuple = {
    (1):frozenset({2,3,4}),
    (2):frozenset({1,3,4}),
    (3):frozenset({1,2,4}),
    (4):frozenset({1,2,3})
    }

#combined = {**avaliable_bishop_dict, **avaliable_knight_dict}

#print(combined)
#combined_dict = {():frozenset()}
combined_dict = {}
counter = 0
for i in avaliable_bishop_dict_tuple.keys():
    #print(f'Position of bishop is {k}')
    for j in avaliable_knight_dict_tuple.keys():
        #print(f'Position of knight on board is {i}')
        if (j!=i) and (j in avaliable_bishop_dict_tuple.get(i)):
            #print('they do not share a position')
            #print(f'b is at {k} and n is at {i}')
            #updated combined dict where key is [k append i value is intersection of k and i 
            #combined_dict.update((i,k): "cheese")
            #print(avaliable_bishop_dict_tuple.get(k))
            combined_dict[(j,i)] = avaliable_bishop_dict_tuple.get(j).intersection(avaliable_knight_dict_tuple.get(i))

#print(len(combined_dict))

avaliable_knight_dict_tuple = {
    (1):frozenset({2,3,4}),
    (2):frozenset({1,3,4}),
    (3):frozenset({1,2,4}),
    (4):frozenset({1,2,3})
    }

combined_dict_2={}
# {(1, 2): frozenset({3}), (1, 3): frozenset({2}) ...
for i in combined_dict.keys():  # i = (1, 2)
    # For each tuple element
    #print(avaliable_knight_2_dict_tuple.keys())
    for j in avaliable_knight_dict_tuple.keys():
        if (j not in i) and (j in combined_dict.get(i)):

            new_position = (j,)
            new_taken = i+new_position

            combined_dict_2[new_taken] = combined_dict.get(i).intersection(avaliable_knight_dict_tuple.get(j))
   # else:
   #     combined_dict_2[(i,k)] = combined_dict.get(i).intersection(avaliable_knight_2_dict_tuple.get(k))
   #     print(combined_dict_2)
#print(f'for k in {avaliable_bishop_dict_tuple.keys()}')
#print(f'{avaliable_knight_dict_tuple}')

print(len(combined_dict_2))
print(combined_dict_2)