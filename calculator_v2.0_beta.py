x = 0
res = 0
i = 0

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

def root(a, b):
    return pow(a, b)

def factorial(a):
    if a == 1:
        return 1
    else:
        return a * factorial(a - 1)

while True: 
    x = res
    while i == 0:
        x = float(input('Enter a number: '))
        i += 1
    operator = input('Select an opreation: ')
    
    if operator == 'Stop' or operator == 'stop':
        break
    
    #addition
    elif operator == '+':
        num = float(input('Enter a number: '))
        res = addition(x, num)
        print(res)
    
    #subctraction
    elif operator == '-':
        num = float(input('Enter a number: '))
        res = subtraction(x, num)
        print(res)
    
    #multiplication
    elif operator == '*':
        num = float(input('Enter a number: '))
        res = multiplication(x, num)
        print(res)
    
    #division
    elif operator == '/':
        num = 0
        while num == 0:
            num = float(input('Enter a number: '))
            if num == 0:
                print('Invalid number')
            else:
                res = division(x, num)
                print(res)
    
    #power
    elif operator == 'pow':
        exp = int(input('Enter an exponent: '))
        res = power(x, exp)
        print(res)
    
    #root
    elif operator == 'root':
        indx = 1.0 / float(input('Enter an index: '))
        res = root(x, indx)
        print(res)
    
    #factorial
    elif operator == '!':
        res = factorial(x)
        print(res)
    
    else:
        print('Invalid operation')