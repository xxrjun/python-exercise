def C(n, m):
    if n == m or m == 0:
        return 1
    else :
        return C(n-1, m-1) + C(n-1, m)
    
while True:
    n = eval(input('n = '))
    m = eval(input('m = '))
    if n>=0 and m>=0 and n>m:
        break
    else:
        print('輸入資料不符, 請重新輸入...')

ans = C(n, m)
print('組合 C(%d, %d) = %d' %(n, m, ans))