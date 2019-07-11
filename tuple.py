def partition():
    
    x = int(input("Enter Your Number: "))
    
    if x % 2 == 0 :
        print("(", x, " none )")
    else :
         print("( none", x, ")")
         
partition()


def laylow():
    
    even_nums = []
    odd_nums = []
    
    lay = int(input("Please Enter A Number"))
    low = int(input("Please Enter Another Number"))
    
    for penzy in range(lay, low):
    
        if penzy % 2 == 0 :
            even_nums.append(penzy)
            
        else :
            odd_nums.append(penzy)
             
             
    print(even_nums)
    print(odd_nums)

laylow()
            