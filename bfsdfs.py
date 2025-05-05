from collections import deque
class graph:
    def __init__(self):
       self.graph={}
    def addedge(self,u,v):
          if u not in self.graph:
            self.graph[u]=[]

          if v not in self.graph:
              self.graph[v]=[]
          self.graph[u].append(v)
          self.graph[v].append(u)
        
    def dfs(self,start):
       visited=set()
       def dfsrecursive(node):
          print(node, end="   ")
          visited.add(node)
          for neighbor in self.graph[node]:
               if neighbor not in visited:
                  dfsrecursive(neighbor)
       dfsrecursive(start)

    def  bfs(self,start):
          visited=set()
          queue=deque()

          visited.add(start)
          queue.append(start)
          while queue:
             node=queue.popleft()
             print(node, end="  ")
             for neigh in self.graph[node]:
                if neigh not in visited:
                   queue.append(neigh)
                   visited.add(neigh)

def main():
   g=graph()
   n=int(input("Enter no of edges "))
   for _ in range(n):
      u,v=map(int,input("Enter edges (u,v) seperetd by spaces ").split())
      g.addedge(u,v)

   start=int(input("enetr starting vertex"))
   print("\n\ndfs")
   g.dfs(start)

   print("\n\n Bfs")
   g.bfs(start)

if __name__=="__main__":
  main()




 
