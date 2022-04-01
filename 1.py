A =  [[0 for x in range(9)] for y in range(9)]
for i in range(9):
    for j in range(9):
        A[i][j] = (i+1)*(j+1)
        print(' %3d' %A[i][j], end='')
    print()
