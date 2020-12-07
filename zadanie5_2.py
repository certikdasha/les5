def sq (chislo):
    return chislo ** 2

def pr(ch):
    for i in range(2, int(ch)):
        if ch % i == 0:
            return None
    return ch 

numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

l = list(map(pr, range(1,30)))
li = []
for i in l:
    if i != None:
        li.append(i)

squ = list(map(sq, li))

print(squ)



