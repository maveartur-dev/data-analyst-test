"""Check if two strings are isomorphic

Two strings are isomorphic if each character in the first string can be
replaced to get the second string, with a one-to-one mapping

Example:
s = "paper", t = "title" -> True
"""

from __future__ import annotations

import argparse


def is_isomorphic(s: str, t: str) -> bool:
    """Return True if strings s and t are isomorphic

    Approach:
    - Maintain forward and backward mappings for bijection
    - Verify consistency for each character pair

    Complexity:
    - Time: O(n)
    - Space: O(1) for fixed alphabet, O(n) in worst case
    """
    if len(s) != len(t):
        return False

    forward: dict[str, str] = {}
    backward: dict[str, str] = {}

    for ch_s, ch_t in zip(s, t):
        # Ensure forward mapping consistency
        if ch_s in forward and forward[ch_s] != ch_t:
            return False
        # Ensure backward mapping consistency
        if ch_t in backward and backward[ch_t] != ch_s:
            return False

        forward[ch_s] = ch_t
        backward[ch_t] = ch_s

    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Check isomorphism of two strings.")
    parser.add_argument("--s", required=True, help="First string")
    parser.add_argument("--t", required=True, help="Second string")
    args = parser.parse_args()

    print(is_isomorphic(args.s, args.t))


if __name__ == "__main__":
    main()
