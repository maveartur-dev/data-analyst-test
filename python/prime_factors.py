"""Compute prime factorization of a positive integer.

Example:
n = 56 -> [2, 2, 2, 7]
"""

from __future__ import annotations

import argparse
from typing import List


def prime_factors(n: int) -> List[int]:
    """Return list of prime factors of n.

    Approach:
    - Divide by 2 while possible.
    - Then trial divide by odd numbers up to sqrt(n).

    Complexity:
    - Time: O(sqrt(n)) in worst case
    - Space: O(1) extra (output excluded)
    """
    if n <= 1:
        return []

    factors: List[int] = []

    # Extract factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Extract odd factors
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2

    if n > 1:
        factors.append(n)

    return factors


def main() -> None:
    parser = argparse.ArgumentParser(description="Prime factorization.")
    parser.add_argument("--n", type=int, required=True, help="Positive integer")
    args = parser.parse_args()

    print(prime_factors(args.n))


if __name__ == "__main__":
    main()
