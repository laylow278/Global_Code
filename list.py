list = []
list.append(input("Enter any string"))

print(list)


#z = [x * 10 if x % 2 == 0 else 0 for x in range(x, y)]
#print(z)

def get_evens(x, y):
    even_nums = []
    print("The Maximum Number is ",max(x, y))
    print("The Minimum Number is ",min(x, y))

    for x in range(x, y):
        if x % 2 == 0:
            even_nums.append(x,)
    return even_nums
            
print(get_evens(int(input("Please Enter any Number")),int(input("Please Another Number"))))

print(get_evens(1, 10))
results = get_evens(15, 30)
print(results)


    