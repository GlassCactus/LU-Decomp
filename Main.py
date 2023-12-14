# Snake Witches
# I like oranges

from fractions import Fraction

def printMatrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()

def printSol(x, n):
    for i in range(n):
        print(x[i][0], end="")
        print()


def LUdecomposition(matrix, n, m):
    L = [[0] * n for i in range(n)]
    U = [[0] * m for i in range(n)]

    for i in range(n):
        L[i][i] = 1

    for k in range(m):
        U[k][k] = matrix[k][k]
        i = k + 1

        while i < m:
            L[i][k] = matrix[i][k] / U[k][k]
            U[k][i] = matrix[k][i]
            i += 1

        i = k + 1

        while i < n:
            j = k + 1

            while j < m:
                matrix[i][j] = matrix[i][j] - (L[i][k] * U[k][j])
                j += 1

            i += 1

    return L, U

def LUsolve(L, U, b, x, n, m):

    y = [[0] for i in range(n)]

    # Forward Substitution
    for i in range(n):
        j = 0
        tempSum = 0

        while j < i:
            tempSum += L[i][j] * y[j][0]
            j += 1

        y[i][0] = b[i][0] - tempSum

    # Backward Substitution (wORK PLEASE)
    for i in range(m):
        i = (m - 1) - i
        j = i + 1
        tempSum = 0

        while j < m:
            tempSum += U[i][j] * x[j][0]
            j += 1

        x[i][0] = (y[i][0] - tempSum) / U[i][i]

    return x


if __name__ == "__main__":
    f = open("input.txt", "r")
    m = 0
    for i in f:
        if i != "\n":
            m += 1
    m -= 1
    f.close()

    f = open("input.txt", "r")
    firstLine = f.readline().split(":")
    n = len(firstLine)
    b = [[0] for i in range(n)]
    x = [[0] for i in range(m) ]
    matrix = [[0] * n for i in range(n)]

    for i in range(n):
        b[i][0] = int(firstLine[i])

    for i in range(m):
        nextLine = f.readline().split(":")
        for j in range(n):
            matrix[j][i] = int(nextLine[j])

    f.close()

    L, U = LUdecomposition(matrix, n, m)
    x = LUsolve(L, U, b, x, n, m)

    ratio = (Fraction(x[0][0]).limit_denominator())
    ratio = int(ratio.denominator)

    for i in range(m):
        x[i][0] = int(round(x[i][0] * ratio))

    #printSol(x, m)

    f = open("output.txt", "w+")

    for i in range(m):
        f.write("%d\n" % x[i][0])

    f.close()
