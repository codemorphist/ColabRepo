cahed = {0: 1, 1: 1}
def fac(n: int) -> int:
    if n in cahed:
        return cahed[n]
    else:
        res = n * fac(n-1)
        cahed[n] = res
        return res

def is_five_exp(n: int) -> bool:
	while n >= 5:
		n //= 5
	return n == 1
