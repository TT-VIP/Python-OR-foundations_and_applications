import math

def NeighborhoodSizeK(n, k):
    return (n - k + 1) * (n - k) - max(0, n - 2*k + 1)

def NeighborhoodSizeStudent(n, k):
    return k^2-2*k*n+k+n^2-1

nMax = 20
kMax = 20
for n in range(1, nMax):
    totalNeighborsN = 0
    totalNeighborsStudent = 0
    for k in range(1, kMax):
        if k < n:
            sizeExpected = NeighborhoodSizeK(n, k)
            sizeStudent = NeighborhoodSizeStudent(n, k)
            if sizeExpected != sizeStudent:
                print(f'n = {n}, k = {k}: {sizeExpected} / {sizeStudent}')

            totalNeighborsN += sizeExpected
            totalNeighborsStudent = sizeStudent

    print(f'Total neighbors = {totalNeighborsN} / {totalNeighborsStudent}')