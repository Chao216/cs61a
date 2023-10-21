kids = {'chao':26,'jiawei':24,'huangzhong':31}

for i in kids.keys():
    print(i)

for j in kids.values():
    print(j)

for k in kids.items():
    print(k)

for i,j in zip(kids.keys(),kids.values()):
    print(i, ' is now ',j, ' years old!')