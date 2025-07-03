
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

def generate_rsa_keys() -> Tuple[Tuple[int, int], Tuple[int, int]]:

    p = int(input("Введите простое p: "))
    q = int(input("Введите простое q: "))

    if not is_prime(p) or not is_prime(q):
        raise ValueError("p и q должны быть простыми числами")

    n = p * q
    phi = (p - 1) * (q - 1)
    print(f"[Keys] n = {n}, phi(n) = {phi}")

    preferred = 65537
    if preferred < phi and gcd(preferred, phi) == 1:
        e = preferred
    else:
        e = next((i for i in range(2, phi) if gcd(i, phi) == 1), None)
        if e is None:
            raise RuntimeError("Не найдено подходящего e")

    d = mod_inverse(e, phi)
    print(f"[Keys] Вычислен d = {d}")

    return (e, n), (d, n)


def rsa_encrypt(m: int, pubkey: Tuple[int, int]) -> int:
    e, n = pubkey
    c = pow(m, e, n)
    return c


def rsa_decrypt(c: int, privkey: Tuple[int, int]) -> int:
    d, n = privkey
    m = pow(c, d, n)
    print(f"[Decrypt] c^{d} mod {n} = {m}")
    return m


raise RuntimeError("Общие секреты не совпадают")

def diffie_hellman_exchange() -> int:
    p = int(input("Простой модуль p: "))
    g = int(input("Генератор g: "))

    if not is_prime(p):
        raise ValueError("p должен быть простым")

    a = int(input("Ваш секрет a: "))
    b = int(input("Секрет партнера b: "))

    A = pow(g, a, p)
    B = pow(g, b, p)
    print(f"[DH] A = g^a mod p = {A}")
    print(f"[DH] B = g^b mod p = {B}")

    s1 = pow(B, a, p)
    s2 = pow(A, b, p)
    print(f"[DH] s1 = B^a mod p = {s1}")
    print(f"[DH] s2 = A^b mod p = {s2}")

    if s1 != s2:
        raise RuntimeError("Общие секреты не совпадают")
    return s1

def main() -> None:


if __name__ == "__main__":
    main()
