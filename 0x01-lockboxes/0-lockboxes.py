#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    stack = [0]  # Start with box 0, which is unlocked by default
    visited[0] = True

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if not visited[key]:
                stack.append(key)
                visited[key] = True

    return all(visited)
