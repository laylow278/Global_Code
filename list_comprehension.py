#sentence = "the quick brown fox jumps over the lazy dog"
#words = sentence.split()

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
even = []
#a = [even.append(x) if x % 2 == 0 for x in numbers]
b = [even for even in numbers if even > 0]
print(b)