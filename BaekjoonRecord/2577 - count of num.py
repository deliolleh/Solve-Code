A = int(input())
B = int(input())
C = int(input())
D = list(str(A*B*C))


for i in range(0,10):
    E = str(i)
    print(D.count(E))