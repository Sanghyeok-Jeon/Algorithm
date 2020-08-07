for i in range(5):
    for j in range(5):
        if i == j:
            c = '#'
        else:
            c = '+'

        if j == 4:
            print(c)
        else:
            print(c, end='')