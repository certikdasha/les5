def _zip_(*args):
    # m =min(map(len, args))
    s = list(map(lambda i: list(map(lambda x: x[i], args)), range(0, min(map(len, args)))))

    return s

a = [1, 3, 5, 3, 6]
b = [34, 23, 12, 466]
c = ['d', 'fghj', 'vbn']

tes = _zip_(a, b, c)
print(tes)



