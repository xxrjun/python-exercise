def gcd(x, y):
    k = 1
    g = k
    while k <= x and k <= y:
        if x % k == 0 and y % k == 0:
            g = k
        k += 1
    return g

while True:
    a = eval(input('輸入第一個正整數a：'))
    b = eval(input('輸入第二個正整數b：'))
    if (a > 0 and b> 0):
        break
    else:
        print('無效輸入, 請重新輸入...')
        print()

ret = gcd(a,b)
print('a, b 兩整數的GCD為', ret)
