for i in range(1, 1001):
    for j in range(i+1, 1001-i):
        if i*i + j*j == (1000-i-j)*(1000-i-j):
            print(i * j * (1000-i-j))