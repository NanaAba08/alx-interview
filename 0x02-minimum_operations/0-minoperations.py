#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    if n <= 1:
        return 0

    # Initialize a list to store the minimum operations required for each index
    min_ops = [0] * (n + 1)

    for i in range(2, n + 1):
        min_ops[i] = float('inf')
        for j in range(1, i):
            # If i is divisible by j, we can achieve i by copying j times and pasting (i // j) - 1 times
            if i % j == 0:
                min_ops[i] = min(min_ops[i], min_ops[j] + i // j)

    return min_ops[n] if min_ops[n] != float('inf') else 0
