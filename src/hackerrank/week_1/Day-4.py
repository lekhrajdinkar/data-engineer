## character grid, rearrange
"""
a b c
a d e
e f g

col-1 : a a e sorted
col-2 : b d f sorted
col-3 : c e g sorted
"""

def gridChallenge(grid):
    un_sorted_grid = [list(row) for row in grid]
    sorted_grid = [sorted(row) for row in grid]
    print('un-sorted-grid',un_sorted_grid)
    print('sorted-grid',sorted_grid)

    for cols in zip(*sorted_grid):
            if list(cols) != sorted(cols):
                print ("Not Sorted (col-wise)", list(cols), sorted(cols))
                return "NO"
            else:
                print ("Sorted (col-wise)", list(cols), sorted(cols))
    return "YES"



grid1 = ['abc','ade', 'efg']
grid2 = ['abc','ade', 'gfa']
grid3=['eabcd','fghij','olkmn','trpqs','xywuv']
print(gridChallenge(grid2))