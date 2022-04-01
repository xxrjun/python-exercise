A1 = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
A2 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]

print('矩陣翻轉前:')
for i in range(4):
    for j in range(3):
        print('%2d' %A1[i][j], end = '  ')
    print()

# 矩陣翻轉作業
for i in range(4):
    for j in range(3):
        A2[4-1-i][j] = A1[i][j]

print()
print('矩陣翻轉後:')
for i in range(4):
    for j in range(3):
        print('%2d' %A2[i][j], end = '  ')
    print()

