# Simple heuristic: count wrong tiles
def heuristic(state, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal[i][j] and state[i][j] != 0:
                h += 1
    return h

# Find position of 0
def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Move blank (0) up, down, left, right
def possible_moves(state):
    x, y = find_zero(state)
    moves = []
    directions = [(-1,0), (1,0), (0,-1), (0,1)]
    for dx, dy in directions:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            moves.append(new_state)
    return moves

# Print the state and heuristic value
def print_state(state, level, h_val):
    print(f"\nLevel {level} (h = {h_val}):")
    for row in state:
        print(row)

# Simple A* without heapq
def simple_astar(start, goal):
    queue = [(start, 0)]  # (state, level)
    visited = []

    while queue:
        queue.sort(key=lambda x: x[1] + heuristic(x[0], goal))  # sort manually by g+h
        state, level = queue.pop(0)
        h_val = heuristic(state, goal)
        print_state(state, level, h_val)

        if state == goal:
            print("\nGoal reached!")
            return

        visited.append(state)

        for move in possible_moves(state):
            if move not in visited:
                queue.append((move, level+1))

# Input matrix
def input_matrix(name):
    print(f"Enter {name} state (row by row, 0 for blank):")
    matrix = []
    for _ in range(3):
        matrix.append(list(map(int, input().split())))
    return matrix

# Main
start = input_matrix("Start")
goal = input_matrix("Goal")
simple_astar(start, goal)
