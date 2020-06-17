def longestMountain(A):
    state = -1
    maxLen = 0
    record = 0
    for i in range(1, len(A)):
        if state == 0:
            if A[i] > A[i - 1]:
                record += 1
            elif A[i] < A[i - 1]:
                record += 1
                state = 1
            else:
                state = -1
        elif state == 1:
            if A[i] < A[i - 1]:
                record += 1
            else:
                if record > maxLen:
                    maxLen = record
                if A[i] > A[i - 1]:
                    state = 0
                    record = 2
                else:
                    state = -1
        else:
            if A[i] > A[i - 1]:
                state = 0
                record = 2
    if state == 1 and record > maxLen:
        maxLen = record

    return maxLen
longestMountain([1,2,3,2,4])