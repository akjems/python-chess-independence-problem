# Step Back

Whatever I do with the current approach I don't think I can make it 200x. 10x run on multiple cores, maybe 5x by changing my combination creator. Also the assignment shouldn't be taking so long, so there may be a short cut,

## Different approaches

I don't need to know the positions, only how many combinations there are. Therefore calculating each position and then counting them up is the long way round to the answer. So maybe I can get mathematically lucky and find a formula that does it for me or more excitingly, create a neural net that can calculate number of combinations based the training set I can now create using my existing program.

### Mathematically Lucky

Each piece has optimal positions and weakest positions.

On 5x5 Optimal, weak, weaker, weakest, follwoed by how many in each category

* King = 9,6, 4 (4)
* Queen = 17, 14, 13 (4)
* rook = 9, 9, 9, 9 
* bishop = 9, 7, 5 (4)
* knight = 9, 7, 5, 4, 3 (4)

MxN determines what percentage of each pieces location is optimal or weakest.  

### Neural Net

Make sure current program is correct and generate thousands of combinations with (M, N, pieces, number_of_combinations). Stick input and outputs into a neureal net and hope it finds a repeatedable pattern.

### Set removal

Just remove occupied and threatened squares from the start list. This is what I'm doing.