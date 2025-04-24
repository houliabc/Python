w,h,v=[int(i) for i in input().split()]
for i in range(h):
    print('Q'*w)
for i in range(w):
    print('Q'*(w+v))
