def func(bod):
    r = [{} for i in range(9)]
    c = [{} for i in range(9)]
    b = [{} for i in range(9)]
    for i in range(9):
        for j in range(9):
            c = bod[i][j]
            if c != 'X':
                num = int(c)
                box_ind = (i // 3) * 3 + j // 3
                r[i][num] = r[i].get(num, 0) + 1
                c[j][num] = c[j].get(num, 0) + 1
                b[box_ind][num] = b[box_ind].get(num, 0) + 1
                if r[i][num] > 1 or c[j][num] > 1 or b[box_ind][num] > 1:
                    print('false')
                    return
    print('true')
bod = []
for i in range(9):
    s = input()
    bod.append(s)
func(bod)