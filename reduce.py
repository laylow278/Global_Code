from functool import reduce

words = ("Hello","World")

def join_strings(strings):
    return reduce(lambda x, y: x+,' ' +y, strings)
print(join_strings(words))
