n = int(input())
n3 = n%10
n2 = (n%100)//10
n1 = n // 100
if n3 == n1 == n2:
    print('все его цифры одинаковые')
else:
    if n1==n2:
        print('равны 1 и 2 цифры')
    else:
        if n1 == n3:
            print('равны 1 и 3 цифры')
        else:
            if n2 == n3:
                print('равны 2 и 3 цифры')
            else:
                print('нет одинаковых цифр')


