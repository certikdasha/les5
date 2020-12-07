def mini (s):
    return s.lower()

def maxi (s):
    return s.upper()

stroli = ['dfFGHJghj', 'fghjGHJK', 'DFGHJKKgu']

mi = list(map(mini, stroli))

ma = list(map(maxi, stroli))

print(mi)
print(ma)


