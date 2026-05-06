def iteration(x, y, max_iter=256):
    """ This functions returns the number of iterations completed before divergence is reached (abs(zn) > 2) for the iterative function z_i+1 = (z_i)^2 + c, where c = x + iy

    Parameters
    ----------
    x : float or int
        the real axis coordinate of the starting point for the iterations
    y : float or int
        the imaginary axis coordinate of the starting point for the iterations
    max_iter : int
        the maximum number of iterations for the function to run (reaching this is assumed no divergence)

    Returns
    -------
    i : int
        the number of iterations before break was reached in the for loop (divergence) or just max_iter-1 if it did not diverge throughout the for loop
    """
    c = x + y*(1j)
    zn = 0 #z0
    for i in range(max_iter):
        zn = zn**2 + c
        if abs(zn) > 2:
            break
    return i

