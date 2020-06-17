###直接完成建堆和堆排序#大根堆
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
        # 建堆
        while last_par_node >= 0:
            self.adjust_heap(lst, last_par_node, length - 1)
            last_par_node -= 1
        # 堆排序
        while last > 0:
            lst[0], lst[last] = lst[last], lst[0]
            self.adjust_heap(lst, 0, last - 1)
            last -= 1
        return lst
        # list_ = [4, 7, 0, 9, 1, 5, 3, 3, 2, 6]
        # heap_sort(list_)
        # print(list_)

class Large_Root_Heap(object):
    #大根堆
    def Init(self,matrix):
        #根据列表长度，找到最后一个非叶子节点，开始循化到 root 根节点，制作大顶堆
        self.matrix = matrix
        length = len(self.matrix)
        last_par_node = length // 2 - 1
        while last_par_node >= 0:
            self.heap_adjust(self.matrix, last_par_node, length - 1)
            last_par_node -= 1  # 每调整好一个节点，从后往前移动一个节点
        #调整父节点 与孩子大小， 制作大顶堆
        # 索引计算: 0 -->1 --->....
        # 父节点 i   左子节点：偶数:2i +1  右子节点：基数:2i +2  注意：当用长度表示最后一个叶子节点时 记得 -1
        # 从第一个非叶子节点(即最后一个父节点)开始，即 list_.length//2 -1（len(list_)//2 - 1）
        # 开始循环到 root 索引为：0 的第一个根节点， 将所有的根-叶子 调整好，成为一个 大顶堆
    def heap_adjust(self,data, par_node, high):
        new_par_node = par_node
        j = 2*par_node + 1   #取根节点的左孩子， 如果只有一个孩子 high就是左孩子，如果有两个孩子 high 就是右孩子

        while j <= high: #如果 j = high 说明没有右孩子，high就是左孩子
            if j < high and data[j] < data[j+1]: #如果这儿不判断 j < high 可能超出索引
                j += 1 # 一个根节点下，如果有两个孩子，将 j  指向值大的那个孩子
            if data[j] > data[new_par_node]: #如果子节点值大于父节点，就互相交换
                data[new_par_node], data[j] = data[j], data[new_par_node]
                new_par_node = j  #将当前节点，作为父节点，查找他的子树
                j = j * 2 + 1
            else:
                break   # 因为调整是从上到下，所以下面的所有子树肯定是排序好了的
                        #如果调整的父节点依然比下面最大的子节点大，就直接打断循环，堆已经调整好了的
    def heap_sort(self,lst):

        last = len(lst) -1
        while last > 0:
            lst[0], lst[last] = lst[last],lst[0]
            self.heap_adjust(lst, 0, last-1)
            last -= 1
        return lst
    def top_k(self,lst,k):
        p = k
        last = len(lst) - 1
        while last > 0:
            lst[0], lst[last] = lst[last], lst[0]
            self.heap_adjust(lst, 0, last - 1)
            last -= 1
            k -= 1
            if k == 0:
                return lst[-p]
        return lst[-p]
class Small_Root_Heap(object):
    def Init(self,matrix):
        max_index=len(matrix)-1
        parent_max=len(matrix)//2-1
        while parent_max>=0:
            self.heap_adjust(matrix,parent_max,max_index)
            parent_max-=1
    def heap_adjust(self,matrix,parent_node,max_index):
        child_node=parent_node*2+1
        while child_node<=max_index:
            if child_node<max_index and matrix[child_node]>matrix[child_node+1]:
                child_node+=1
            if matrix[parent_node]>matrix[child_node]:
                matrix[parent_node],matrix[child_node]=matrix[child_node],matrix[parent_node]
                parent_node=child_node
                child_node=parent_node*2+1
            else:
                break
    def heap_sort(self,matrix):
        last_index=len(matrix)-1
        while last_index:
            matrix[0],matrix[last_index]=matrix[last_index],matrix[0]
            last_index-=1
            self.heap_adjust(matrix,0,last_index)
        return matrix

from heapq import *
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Large_Root_Heap().Init(nums)
        return Large_Root_Heap().top_k(nums,k)
    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0
        heap = []
        for i in range(len(nums)):
            heappush(heap,nums[i])
            if len(heap) > k:
                heappop(heap)
        return heap[0]
print(Solution().findKthLargest([2,1],2))
