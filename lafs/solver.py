import lafs

def linsolve(A, b):
    return lafs.gauss.inv(A) * b
