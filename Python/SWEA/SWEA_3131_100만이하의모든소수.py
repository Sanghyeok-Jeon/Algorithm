prime_num = []
check = [1, 1] + [0] * (10**6 - 1)
for i in range(10**6 + 1):
    if check[i] == 0:
        prime_num.append(i)

        j = 1
        while i * j < 10**6+1:
            if check[i * j] == 0:
                check[i * j] = 1
            j += 1

for i in range(len(prime_num)):
    print(prime_num[i], end=' ')
