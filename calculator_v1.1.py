x = 0
res = 0
i = 0
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
        res = x + num
        print(res)
    
    #subctraction
    elif operator == '-':
        num = float(input('Enter a number: '))
        res = x - num
        print(res)
    
    #multiplication
    elif operator == '*':
        num = float(input('Enter a number: '))
        res = x * num
        print(res)
    
    #division
    elif operator == '/':
        num = 0
        while num == 0:
            num = float(input('Enter a number: '))
            if num == 0:
                print('Invalid number')
            else:
                res = x / num
                print(res)
    
    #power
    elif operator == 'pow':
        num = float(input('Enter a number: '))
        exp = int(input('Enter an exponent: '))
        res = pow(num, exp)
        print(res)
    
    #root
    elif operator == 'root':
        num = float(input('Enter a number: '))
        indx = int(input('Enter an index: '))
        res = pow(num, 1/indx)
        print(res)
    
    #factorial
    elif operator == '!':
        num = res
        fact = 1
        n = 1
        while n <= num:
            fact *= n
            n += 1
        res = fact
        print(res)
    
    else:
        print('Invalid operation')