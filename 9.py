def series(a, d, n):
     if n <= 0:
         return 0
     else:
         return a+(n-1)*d + series(a, d, n-1)
     
a = eval(input('首項 a = '))
d = eval(input('公差 d = '))
n = eval(input('項數 n = '))
sum = series(a, d, n)
print('等差數列的總和為 ', sum)