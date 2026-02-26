"""Find the missing number from the sequence 1..n

Input contains distinct integers from 1 to n with one missing

Example:
nums = [1, 2, 3, 4, 5, 6, 8, 9, 10, 11] -> 7
"""

from __future__ import annotations

import argparse
from typing import List


def missing_number(nums: List[int]) -> int:
    """Return the missing number in the range 1..n

    Approach:
    - Use arithmetic series sum
    - n is inferred as len(nums) + 1

    Complexity:
    - Time: O(n)
    - Space: O(1)
    """
    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def main() -> None:
    parser = argparse.ArgumentParser(description="Find missing number in 1..n.")
    parser.add_argument("--nums", nargs="+", type=int, required=True, help="Numbers list")
    args = parser.parse_args()

    print(missing_number(args.nums))


if __name__ == "__main__":
    main()
