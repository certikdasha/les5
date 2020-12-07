
f = open('FB.txt', 'r')
r = open('result2.txt', 'w')

def parse_line(line):
    e = line.split()
    return int(e[0]), int(e[1]), int(e[2])


def calc_fb(fir, sec, i):
    if (i % fir == 0) and (i % sec == 0):
        return 'FB'
    elif(i % fir == 0):
        return 'F'   
    elif(i % sec == 0):
        return 'B'
    else:
        return str(i)


def fizzbuzz(fir, sec, col):

    return ' '.join(map(lambda x: calc_fb(fir, sec, x), range(1, col + 1)))


for line in f:
    fi, s, c = parse_line(line)


    r.writelines(f'Initial data: {fi, s, c} \n')
    r.writelines(fizzbuzz(fi, s, c) + '\n\n')   

f.close()
r.close()