import math
x = 0
res = 0
while True: 
    x = res
    operator = input('Select an opreation: ')
    
    if operator == 'Stop' or operator == 'stop':
        break
    
    elif operator == '=':
        print(x)
    
    elif operator == '+':
        num = float(input('Enter a number: '))
        res = x + num
    
    elif operator == '-':
        num = float(input('Enter a number: '))
        res = x - num
    
    elif operator == '*':
        num = float(input('Enter a number: '))
        res = x * num
    
    elif operator == '/':
        num = float(input('Enter a number: '))
        res = x / num
    
    elif operator == 'pow':
        num = float(input('Enter a number: '))
        exp = int(input('Enter an exponent: '))
        res = pow(num, exp)
    
    elif operator == 'sqrt':
        num = float(input('Enter a number: '))
        res = math.sqrt(num)
    
    elif operator == '!':
        num = range(1, int(input('Enter a number: ')) + 1)
        fact = 1
        for n in num:
            fact *= n
        res = fact
    
    else:
        print('Invalid operation')