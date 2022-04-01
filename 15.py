def binary_search(data, key):
    #設置選取範圍的指標
    low = 0
    upper = len(data) - 1
    while low <= upper:
        mid = (low + upper) // 2  #取中間索引的值
        if data[mid] < key:    #若搜尋值比中間的值大，將中間索引+1，取右半
            low = mid + 1
        elif data[mid] > key:  #若搜尋值比中間的值小，將中間索引+1，取左半
            upper = mid - 1
        else:                    #若搜尋值等於中間的值，則回傳
            return mid
    return -1

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = int(input('輸入要搜尋的數值：'))
index = binary_search(data, target)
if index >= 0:
    print("找到數值 {} 於索引：".format(target) + str(index))
else:
    print("找不到數值！")