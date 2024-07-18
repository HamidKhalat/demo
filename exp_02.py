a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [6]
c = []

for i in a:
    c.append([i] + b)

print(c)