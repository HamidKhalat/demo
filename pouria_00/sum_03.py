# sum odd numbers from 1 to 100
# a = [1,2,3,4,5]
# b = 3
# c = []
# d = [i + b for i in a]
C = 0
for i in range(100):
    if i % 2 == 1:
        C = i + C

print (C)
    # c.append(i+b)