def printnum(n):
    line = 0
    print()
    print('1~%d 的質數如下：' %n)
    for i in range(2, n+1):
        flag = 0
        for j in range(2, i):
            if i % j == 0:
                flag = 1
        if flag == 0:
            print('%5d' %i , end='')
            line = line + 1
            if line % 10 == 0:
                print()

num = eval(input('求質數，請輸入一個數：'))
printnum(num)