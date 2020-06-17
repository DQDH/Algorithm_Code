def min_max_num(n,nums):
    if nums.count(nums[0]) == n:
        print(' '.join([str(n * (n - 1) // 2), str(n * (n - 1) // 2)]))
    else:
        same_count = 1
        same_count_list = []
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                same_count += 1
            else:
                same_count_list.append(same_count)
                same_count = 1
        if same_count > 1:
            same_count_list.append(same_count)
        combination = 0
        for each in same_count_list:
            if each > 1:
                combination += each * (each - 1) // 2
        if combination:
            minimum_count = combination
        else:
            diffs = [abs(nums[i] - nums[i + 1]) for i in range(n - 1)]
            minimum_count = diffs.count(min(diffs))
        maximum_count = nums.count(nums[0]) * nums.count(nums[n - 1])
        return minimum_count,maximum_count

while True:
    try:
        n = int(input())
        nums = [each for each in map(int, input().split())]
        minimum_count, maximum_count=min_max_num(n,sorted(nums))
        print(' '.join([str(minimum_count), str(maximum_count)]))
    except:
        pass