import sys
def row_list_w(m):
    row = list()
    for j in range(m):
        if j % 2 == 0:
            row.append(0)
        else:
            row.append(1)
    return row
def row_list_b(m):
    row = list()
    for j in range(m):
        if j % 2 == 0:
            row.append(1)
        else:
            row.append(0)
    return row

def arr(n, m):
    arr = list()
    for i in range(n):
        if i % 2 == 0:
            row = row_list_w(m)
            arr.append(row)
        else:
            row = row_list_b(m)
            arr.append(row)
    return arr


def cn(x1, y1, x2, y2, arrays, judge=0):
    for i in range(x1-1, x2):
        for j in range(y1-1, y2):
            if judge:
                arrays[i][j] = 1
            else:
                arrays[i][j] = 0
    return arrays

def count(n, m, color_):
    summ = n*m
    l = []
    for i in range(n):
        l += color_[i]
    black = sum(l)
    white = summ - black
    return white, black

def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

if __name__ == '__main__':
    n = input()
    T = int(n)
    sum_list = []
    for i, line in enumerate(sys.stdin):
        s = line.split()
        if i % 3 == 0:
            tmp = s
        elif i % 2 == 0:
            tmp.extend(s)
        else:
            tmp.extend(s)
            sum_list.append(tmp)
    for list_ in sum_list:
        n, m = int(list_[0]), int(list_[1])
        x1, y1, x2, y2 = int(list_[2]), int(list_[3]), int(list_[4]), int(list_[5])
        x1_, y1_, x2_, y2_ = int(list_[6]), int(list_[7]), int(list_[8]), int(list_[9])
        a = arr(n, m)
        out = cn(x1, y1, x2, y2, a, 0)
        out = cn(x1_, y1_, x2_, y2_, out, 1)
        w, b = count(n, m, out)
        print(w, b)
