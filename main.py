
import math
from typing import Tuple

def is_prime(n: int) -> bool:

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    limit = int(math.sqrt(n)) + 1
    for divisor in range(3, limit, 2):
        if n % divisor == 0:
            print(f"[is_prime] {n} делится на {divisor}")
            return False
    return True


def gcd(a: int, b: int) -> int:

    while b:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:

    if b == 0:
        return (1, 0, a)
    x1, y1, d = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return x, y, d


def mod_inverse(e: int, phi: int) -> int:

    x, y, g = extended_gcd(e, phi)
    if g != 1:
        raise ArithmeticError("Обратного элемента не существует")
    return x % phi


def main() -> None:


if __name__ == "__main__":
    main()
