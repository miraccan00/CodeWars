costs1 = [[1,3,4,5], 
         [2,3,2,3], 
         [3,1,4,1],
         [2,3,1,3]]

costs2 = [[2, 10, 4, 1],
          [10, 7, 10, 3],
          [6, 7, 10, 7],
          [9, 7, 6, 10],
          [4, 2, 7, 10],
          [9, 4, 1, 5]]
#print(costs1[i][j],end=' ')
#1 3 4 5 2 3 2 3 3 1 4 1 2 3 1 3
#print(costs1[i],end=' ')
#[1, 3, 4, 5] [2, 3, 2, 3] [3, 1, 4, 1] [2, 3, 1, 3]

def paint_tiles(costs):
    counter=0
    for i in range(len(costs)):
        counter+=min(costs[i])
    return counter
    


print(paint_tiles(costs1))
print(paint_tiles(costs2))
