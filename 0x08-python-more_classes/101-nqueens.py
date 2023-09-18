#!/usr/bin/python3
"""
A program to print all the possible solution to
N queens puzzle problem
"""
import sys


def is_valid_state(state, n):
    return len(state) == n


def get_candidates(state, n):
    if not state:
        return range(n)
    position = len(state)
    candidates = set(range(n))
    for row, col in enumerate(state):
        candidates.discard(col)
        dist = position - row
        candidates.discard(col + dist)
        candidates.discard(col - dist)
    return candidates


def search(state, solutions, n):
    if is_valid_state(state, n):
        solutions.append(list(state))
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not args[1].isdigit():
        print("N must be a number")
        exit(1)
    if int(args[1]) < 4:
        print("N must be at least 4")
        exit(1)

    n = int(args[1])
    solutions = []
    state = []
    search(state, solutions, n)
    output = []

    for solution in solutions:
        inner = []
        for item in solution:
            inner.append(list((solution.index(item), item)))
        output.append(inner)

    for item in output:
        print(item)
