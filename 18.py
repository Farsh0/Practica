a = [i for i in range(1,21)]
for i in range(len(a)):
    if a[i] % 2 == 0:
        a[i] == a[i]**2
    else:
        a[i] == a[i]+2
print(a)


print([i**2 if i%2 == 0 else i+2 for i in range(1,21)])