def extendGCD(a,b):     #Rozszerzony algorytm Euklidesa
    u,w,x,z = 1,a,0,b
    while w:
        if w < z:
            q = u
            u = x
            x = q
            q = w
            w = z
            z = q
        q = w // z
        u -= q * x
        w -= q * z
    if z == 1:
        if x < 0: x += b
        return x
    else:
        print("BRAK")


def montgomery(A, B, N):        # N musi byc > R oraz N > 3 i nieparzyste oraz NWD(R, N) > 1
    R = 2
    while(R<N):                 #Obliczenie R
        R*=2

    am = (A * R) % N            # A w przestrzeni Montogomeryego
    bm = (B * R) % N            # B w przestrzeni Montogomeryego
    x = (am * bm)               # x = (AB)'
    a = N                       # pomocnicza
    b = R                       # pomocnicza
    rR = extendGCD(a,b)         # R^-1
    rR = R - rR
    nR = extendGCD(b,a)         # N^-1
    s = (x * rR) % R
    u = (x + s * N) // R
    if u < N:
        cm = u
    else:
        cm = u - N

    return (cm * nR) % N       # Wynik już na normalnej liczbnie
