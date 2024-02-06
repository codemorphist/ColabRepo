cahed = {0: 1, 1: 1}
def fac(n: int) -> int:
    if n in cahed:
        return cahed[n]
    else:
        res = n * fac(n-1)
        cahed[n] = res
        return res

def isPrime(n: int):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

