import math

def column(position,number_of_columns):
    if position%number_of_columns == 0:
    # It's in the last column not 0 column
        current_column=number_of_columns
    else:
        current_column = (position%number_of_columns)
    return(current_column)