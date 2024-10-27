L = []
with open('temp3.txt','r') as f:
    for i in range(49):
        c = f.readline()
        c = eval(c)
        L.append(c[1])
print(L)
print(list([x for x in L if L.count(x) == 1]))