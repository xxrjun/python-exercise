def GCD(p, q):
    if (p == 0 or q == 0):
        return 0
    else :
        rem = p % q
        if (rem == 0):
            return q
        else :
            return GCD(q, rem)

n1 = 60
n2 = 96
res = GCD(n1, n2)
print('GCD(%d, %d) = %d' %(n1, n2, res))
