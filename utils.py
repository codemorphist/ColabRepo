cahed = {0: 1, 1: 1}
def fac(n: int) -> int:
    if n in cahed:
        return cahed[n]
    else:
        res = n * fac(n-1)
        cahed[n] = res
        return res

def GCD(a, b)
    if a < b:
        a, b = b, a
    if not b:
        return a
    return GCD(b, a % b)
