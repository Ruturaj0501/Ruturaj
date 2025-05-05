# Function to check if placing a queen at (row, col) is safe
def isSafe(board, row, col):
    for i in range(row):
        # Check same column
        if board[i] == col:
            return False
        # Check diagonals
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

# Backtracking method
def nQueens_backtracking(n):
    board = [-1] * n
    solutions = []

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if isSafe(board, row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1  # Backtrack

    solve(0)
    return solutions

# Branch and Bound method (faster checking using arrays)
def nQueens_branch_bound(n):
    board = [-1] * n
    solutions = []

    col_used = [False] * n
    diag1_used = [False] * (2 * n)
    diag2_used = [False] * (2 * n)

    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        for col in range(n):
            if not col_used[col] and not diag1_used[row + col] and not diag2_used[row - col + n]:
                board[row] = col
                col_used[col] = diag1_used[row + col] = diag2_used[row - col + n] = True
                solve(row + 1)
                col_used[col] = diag1_used[row + col] = diag2_used[row - col + n] = False

    solve(0)
    return solutions

# Function to print the board solution
def print_solution(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

# Main function
def main():
    n = int(input("Enter number of queens (n): "))

    print("\nBacktracking Solutions:")
    solutions1 = nQueens_backtracking(n)
    print(f"Total: {len(solutions1)} solutions")
    for sol in solutions1:
        print_solution(sol)

    print("\nBranch and Bound Solutions:")
    solutions2 = nQueens_branch_bound(n)
    print(f"Total: {len(solutions2)} solutions")
    for sol in solutions2:
        print_solution(sol)

if __name__ == "__main__":
    main()
