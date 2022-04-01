def factor(num, div):
    if (num == 1) or (div > num):
        return
    else:
        if(num % div == 0):
            print('%d * ' %div, end = '')
            factor(num/div, div)
        else:
            if (div == 2):
                div = 3
            else:
                div = div + 2
            factor(num, div)
            
number = eval(input('輸入一個數值：'))
print(number, end = ' = ')
factor(number, 2)