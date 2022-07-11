from collections import deque


def merge_sort(nums):
    # used merge sort to sort the input array nums

    n = len(nums)

    # 1. create n sublists
    sublists = deque([[x] for x in nums])

    # 2. merge sublists untill one lists remains
    while len(sublists) > 1:
        A = sublists.popleft()
        B = sublists.popleft()
        sublists.append(merge(A,B))

    return sublists[0]



def merge(A, B):
    # merges the (sub)lists A and B. A and B should already be sorted
    # this functin is of O(min(len(A), len(B)))

    a = 0
    b = 0
    result = []

    while True:
        if A[a] < B[b]:
            result.append(A[a])
            a += 1
        else:
            result.append(B[b])
            b += 1

        if a == len(A):
            result += B[b:]
            break
        elif b == len(B):
            result += A[a:]
            break

    return result

