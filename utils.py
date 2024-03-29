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


def valid_anagram(s: str, t: str) -> bool:
    """
    Function to validate anagram
    """
    if len(s) != len(t):
        return False

    used_symbols = {}

    for ch in s:
        if ch not in used_symbols:
            used_symbols[ch] = 1
        else:
            used_symbols[ch] += 1

    for ch in t:
        if ch not in used_symbols:
            return False
        else:
            used_symbols[ch] -= 1

    for ch in used_symbols:
        if ch: return False
    
    return True


def GCD(a, b)
    if a < b:
        a, b = b, a
    if not b:
        return a
    return GCD(b, a % b)


def is_five_exp(n: int) -> bool:
	while n >= 5:
		n //= 5
	return n == 1


def valid_triangle(a, b, c):
    return a + b > c and a + c > b and c + b > a
