#!/usr/bin/python3
"""
Solution to the N Queens problem.
"""
import sys


def solve_nqueens(row, size, cols, pos_diagonals, neg_diagonals, board):
    """
    Recursive backtracking function to find solutions for the N Queens problem.
    """
    if row == size:
        solution = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for col in range(size):
        if col in cols or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
            continue

        cols.add(col)
        pos_diagonals.add(row + col)
        neg_diagonals.add(row - col)
        board[row][col] = 1

        solve_nqueens(row + 1, size, cols, pos_diagonals, neg_diagonals, board)

        cols.remove(col)
        pos_diagonals.remove(row + col)
        neg_diagonals.remove(row - col)
        board[row][col] = 0


def nqueens(size):
    """
    Initializes the board and sets for solving the N Queens problem.
    """
    columns = set()
    positive_diagonals = set()
    negative_diagonals = set()
    board = [[0] * size for _ in range(size)]

    solve_nqueens(0, size, columns, positive_diagonals,
                  negative_diagonals, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(args[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
