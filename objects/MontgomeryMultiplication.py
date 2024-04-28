class MontgomeryMultiplication:
    multiplicand = []
    multiplier = []

    def montgomery_multiply(a, b, n, s, W):

        t = [0] * (2 * s + 1)
        for i in range(s):
            C = 0
            for j in range(s):
                C, S = (t[i + j] + a[j] * b[i] + C, t[i + j] + a[j] * b[i] + C)
                t[i + j] = S
            t[i + s] += C

        for i in range(s):
            C = 0
            m = t[i] * (n[0] % (2 ** W)) % W
            for j in range(s):
                C, S = (t[i + j] + m * n[j] + C, t[i + j] + m * n[j] + C)
                t[i + j] = S
            t[i + s] += C

        u = t[:]
        for j in range(s):
            u[j] = t[j + s]

        B = 0
        for i in range(s):
            B, D = (u[i] - n[i] - B, u[i] - n[i] - B,)
            t[i] = D
        B, D = (u[s] - B, u[s] - B)
        t[s] = D

        if B == 0:
            return t[:s]
        else:
            return u[:s]

    a = [1, 0]
    b = [4, 0]
    n = [2, 0]
    s = 2
    W = 8

    result = montgomery_multiply(a, b, n, s, W)
    print(result)
