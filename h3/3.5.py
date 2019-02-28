'''
深度优先遍历
Description

按照给定的起始顶点深度优先遍历给定的无向图，尝试所有可能的遍历方式，打印遍历过程中出现的最大深度。


Input

输入第一行是用例个数，后面每个用例使用多行表示，用例的第一行是图中节点的个数n和起始点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。


Output

输出深度优先遍历中遇到的最大深度。


Sample Input 1

1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1

4
'''
import sys

def fuck():
    num = int(sys.stdin.readline().strip())
    for num_test in range(num):
        lines_and_start = sys.stdin.readline().strip().split(" ")
        lines = int(lines_and_start[0])
        start = lines_and_start[1]
        start_i = 0
       # print(lines,start)
        row =  sys.stdin.readline().strip().split(" ")
        juzheng = [ [0] * (len(row) ) for x in range(len(row))]
        #juzheng[0] = row
       # print(juzheng)
        for i in range(len(row)):
            tmp = sys.stdin.readline().strip().split(" ") 
            juzheng[i] = tmp

          #  print(tmp)
            if start == tmp[0]:
                start_i = i
        #print(juzheng)
        for j in range(len(juzheng)):
            juzheng[j] = juzheng[j][1:]
        #print(juzheng)
        return start_i, row , juzheng 


class Graph:
    def __init__(self, nodes , edges):
        self.nodes = nodes
        self.edges = edges

    def getFirst(self,c):
        i = self.nodes.index(c)
        
        for x in range(len(self.edges[i])):
            if self.edges[i][x] == "1":
                return self.nodes[x],x
        return 'x',-1 
       

    def getNext(self,c,now):
        i = self.nodes.index(c)
        if now >= len(self.edges) - 1:
            return 'x',-1 
        for  x in range(now + 1,len(self.edges)):
            if self.edges[i][x] == '1':
                return self.nodes[x],x
        return 'x',-1 

    def show(self):
        print(self.nodes)
        print(self.edges)

def DFS(graph, queue, visited , c):
    queue.append(c)
    visited[c] = True
    m = graph.getFirst(c)
    while( m[1] != -1):
        if not visited[m[0]]:
            visited[m[0]] = False
            DFS(graph, queue, visited, m[0])
        else:
            m = graph.getNext(c,m[1])
    

if __name__ == "__main__":
    start_i, row, juzheng = fuck()
    graph = Graph(row, juzheng)
    visited = dict()
    for i in graph.nodes:
        visited[i] = False
    queue = list()
    DFS(graph,queue,visited,row[start_i])
    
    for i in queue:
        print(i,end=" ")







