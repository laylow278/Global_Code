print("ln Next one")

for j in [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]:
    print(j)



print("ln Next one")

def star():
    a = 1
    while a < 5:
        print("****")
        a += 1
star()





def star():
    for i in range(0,4):
        for j in range(0, i+1):
            print("*",end = "")
        print()
    for i in reversed(range(0,3)):
        for j in range(0, i+1):
            print("*",end = "")
        print() 
star()


