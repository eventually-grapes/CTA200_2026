def iteration(x, y, diverge=2, max_iter=256):
    c = x + y*(1j)
    zn = 0 #z0
    for i in range(max_iter):
        zn = zn**2 + c
        if abs(zn) > diverge:
            break
    return i

