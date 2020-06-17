class ALL(object):
    def adjust_heap(self,data, par_node, high):
        new_par_node = par_node
        j = 2 * par_node + 1
        while j <= high:
            if j < high and data[j] < data[j + 1]:
                j += 1
            if data[j] > data[new_par_node]:
                data[new_par_node], data[j] = data[j], data[new_par_node]
                new_par_node = j
                j = j * 2 + 1
            else:
                break

    def heap_sort(self,lst):
        length = len(lst)
        last = length - 1
        last_par_node = length // 2 - 1

        while last_par_node >= 0:
            self.adjust_heap(lst, last_par_node, length - 1)
            last_par_node -= 1

        while last > 0:
            lst[0], lst[last] = lst[last], lst[0]
            self.adjust_heap(lst, 0, last - 1)
            last -= 1
        return lst
data=list(map(int,raw_input().split(',')))
print(ALL().heap_sort(data))