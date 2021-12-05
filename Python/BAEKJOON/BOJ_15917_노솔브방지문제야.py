twos = [2**i for i in range(0, 32)]
Q = int(input())
for _ in range(Q):
    a = int(input())
    print(1 if a in twos else 0)