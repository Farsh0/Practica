n = int(input())
lst = [64, 32, 16, 8, 4, 2, 1]
ans = []
с = 0
while n > 0:
    for i in lst:
        if n >= i:
            n -= i
            с += 1
            
        ans.append(i)
    break
print(f'Понадобится {с}шт. купюр, а именно:')
print(*ans)
