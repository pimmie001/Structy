def tribonacci(n):
    A = {}
    return tri(n, A)

def tri(n, A):
    if n == 0 or n == 1:
        return 0
    if n == 2:
        return 1

    if n in A:
        return A[n]

    A[n] = tri(n-1, A) + tri(n-2, A) + tri(n-3, A)
    return A[n]

