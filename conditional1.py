def is_odd():
    numbers = [1,56,234,87,4,76,24,69,90,135]
    isEven = []
    
    for x in numbers:
        if not(x % 2 == 0):
            isEven.append(x)
        
    print(isEven)
    
is_odd()
