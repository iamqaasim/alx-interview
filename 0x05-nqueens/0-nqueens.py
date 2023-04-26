#!/usr/bin/python3
'''N Queens Challenge'''

import sys

def print_board(board):
    for row in board:
        print("".join(row))

def is_safe(board, row, col, n):
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == "Q":
            return False
    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    # Check lower diagonal on left side
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False
    return True

def solve(board, col, n):
    # If all queens are placed, print the solution
    if col == n:
        print_board(board)
        print()
        return True
    # Place queen in every row of current column and check if it's safe
    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            res = solve(board, col + 1, n) or res
            board[i][col] = "."
    return res

def n_queens(n):
    # Initialize the board with dots
    board = [["." for x in range(n)] for y in range(n)]
    solve(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    n_queens(n)
