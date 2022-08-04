import math
n = 2000000
a = [True for i in range(n)]
s = 0

if __name__ == "__main__":
    a[0] = a[1] = False;
    for i in range(2,  int(math.sqrt(n)) ):
        if(a[i]):
            s += i;
            for j in range(i*i, int(math.sqrt(n)), i):
                a[j] = False;
    print(s)