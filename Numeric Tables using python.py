#for i in range(12,15):
 #   for j in range(1,11):
  #      print(i,"*",j,"=",i*j)

   
#print()

# i= int(input("Enter a  number"))
# if (i%2!=0):
#     print("weird")
# else:
#     if (i ==range(2,6)):
#         print("not wired")
#     elif(i== range(6,21)):
#         print("weird")
#     elif(i>20):
#         print("not weird")
#     else:
#         print("code end")

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self,u ,v, weight):
        self.edges.append((u,v,weight))

    def find(self, parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])

    def union(self,parent,rank,x,y):
      root_x = self.find(parent,x)
      root_y = self.find(parent,y)
      if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
      elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
      else:
        parent[root_y] = root_x
        rank[root_x] += 1

    def kruskal(self):
        self.edges.sort(key=lambda x:x[2])
        parent = []
        rank = []
        for node in range(self.V):
          parent.append(node)
          rank.append(0)
        mst =[]
        mst_cost = 0
        for edge in self.edges:
          u,v,weight = edge
          root_u = self.find(parent,u)
          root_v = self.find(parent,v)

          if root_u != root_v:
            mst.append(edge)
            mst_cost += weight
            self.union(parent,rank,root_u,root_v)
        return mst,mst_cost
        

g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0,2,8)
g.add_edge(1,2,12)
g.add_edge(2,3,7)

mst,mst_cost = g.kruskal()

print("Edges in the Minimum Spanning tree:")
for u,v, weight in mst:
  print(f"({u},{v}) with weight {weight}")

print("Total cost of the Minimum Spanning tree:",mst_cost)




