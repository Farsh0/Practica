a = ['ddd', 'ddd', 'hgh', 'hjn', 'hjn']
s = 0
for i in a:
    for j in a:
        if i == j:
            s += 1
    s -= 1
print(s/2)
