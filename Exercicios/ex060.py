from math import factorial


c = 0
num = int(input('digite um numero para ver seu factorial: '))
while c <= num:
    c += 1
    if c <= num:
        print(f'{c} x ', end = '')
    if c == num:
        (print(f'{c} = ', end = ''))
        print(factorial(num))
    
   
     
     