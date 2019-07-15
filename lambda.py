
numbers = [1,56,234,87,4,76,24,69,90,135]

lambda a: a % 2 == 0

a = filter(lambda a: a % 2 == 0, numbers)

print(list(a))
