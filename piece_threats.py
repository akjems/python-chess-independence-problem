from edge_checker import column

def king_threats (N,i, current_column, threatened):
    if column(i+1,N) > current_column:
        threatened.add(i+1)
        threatened.add(i+N+1)
        threatened.add(i-N+1)
    if column(i-1,N) < current_column:     
        threatened.add(i-1)
        threatened.add(i+N-1)
        threatened.add(i-N-1)
        
    if column(i+N,N) == current_column:
        threatened.add(i+N)
    if column(i-N,N) == current_column:
        threatened.add(i-N)
    
    return (threatened)

