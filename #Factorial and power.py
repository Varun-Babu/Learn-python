def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)    


def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num - 1)
        
print(fact(5))    
print(power(2,2))
