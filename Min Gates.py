q = []
w = []

l = [630, 645, 730, 1100]
t = [700, 845, 900, 1200]
waitT = 20
init = 1

i , j = 0, 0
count = 0
while i<len(l) and j<len(t):
    print(i,j)
    print(q,w)
    if l[i] > t[j]:
        q.pop(0)
        if w:
            q.append(t[w.pop(0)])
        j += 1
        continue
    if t[j] - l[i] - 40 > waitT:
        q.append(t[i])
        count = len(q) if len(q) > count else count
    else:
        w.append(i)
    i += 1
    
print(count + init) 