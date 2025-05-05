import heapq

# Selection Sort Function
def selection(arr):
    n = len(arr)
    for i in range(n):
        minindex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minindex]:
                minindex = j
        arr[i], arr[minindex] = arr[minindex], arr[i]
    return arr

# Input for Selection Sort
def selec_input():
    n = int(input("\nEnter number of elements: "))
    arr = []
    for i in range(n):
        arr.append(int(input(f"Enter element {i + 1}: ")))
    sorted_arr = selection(arr)
    print("\nSorted elements are:", sorted_arr)

# Prim's Algorithm
def prim(graph, n):
    mst = []
    visited = [False] * n
    minheap = [(0, 0, -1)]  # (weight, current_node, parent)
    total_weight = 0

    while minheap:
        weight, u, parent = heapq.heappop(minheap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight

        if parent != -1:
            mst.append((parent, u, weight))  # Edge: from -> to

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(minheap, (w, v, u))

    return mst, total_weight

# Input for Graph
def takeinput():
    n = int(input("\nEnter number of vertices: "))
    graph = {i: [] for i in range(n)}
    m = int(input("Enter number of edges: "))
    print("Enter the edges in format: vertex1 vertex2 weight")
    for _ in range(m):
        u, v, w = map(int, input("Enter edge: ").split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    return graph, n

# Main Function
def main():
    print("\n1. Selection Sort")
    print("2. Prim's Algorithm")
    ch = int(input("\nEnter your choice (1 or 2): "))
    
    if ch == 1:
        selec_input()
    elif ch == 2:
        graph, n = takeinput()
        mst, total_weight = prim(graph, n)
        print("\nMinimum Spanning Tree edges:")
        for u, v, weight in mst:
            print(f"Edge from {u} to {v} with weight {weight}")
        print(f"\nTotal weight of MST is: {total_weight}")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()