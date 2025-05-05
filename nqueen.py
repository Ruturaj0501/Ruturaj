def n_queens_backtracking(n):
    def is_safe(queens, row, col):
        for i in range(row):
            if queens[i] == col or abs(queens[i] - col) == row - i:
                return False
        return True

    def backtrack(row, queens):
        if row == n:
            solutions.append(queens)
            return
        for col in range(n):
            if is_safe(queens, row, col):
                backtrack(row + 1, queens + [col])

    solutions = []
    backtrack(0, [])
    return solutions

def n_queens_branch_and_bound(n):
    def backtrack(row, queens):
        if row == n:
            solutions.append(queens)
            return
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                backtrack(row + 1, queens + [col])
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    solutions = []
    cols = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)
    backtrack(0, [])
    return solutions

def print_solutions(solutions, n):
    for sol in solutions:
        for r in sol:
            print(" . " * r + " Q " + " . " * (n - r - 1))
        print()

# ----------- Main Program -----------
n = int(input("Enter value of N: "))
method = input("Choose method (backtrack/branch): ").strip().lower()

if method == "backtrack":
    sols = n_queens_backtracking(n)
elif method == "branch":
    sols = n_queens_branch_and_bound(n)
else:
    print("Invalid method.")
    exit()

print(f"\nTotal solutions: {len(sols)}\n")
print_solutions(sols, n)
