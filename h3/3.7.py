'''
广度优先遍历图
Description

按照给定的起始顶点广度优先遍历图，每一次通过字母顺序选择顶点查找下一层邻接点，打印遍历顺序。


Input

输入第一行为测试用例个数，后面每一个用例用多行表示，用例第一行是节点个数n和开始顶点，用空格隔开，后面n+1行为图的邻接矩阵，其中第一行为节点名称。值之间使用空格隔开。


Output

输出遍历顺序，用空格隔开


Sample Input 1

1
4 a
a b c d
a 0 1 1 0
b 1 0 1 0
c 1 1 0 1
d 0 0 1 0
Sample Output 1

a b c d
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

def BFS(graph,c):
    queue_1 = list()
    queue_2 = list()
    queue_1.append(c)
    visited = dict()
    for i in graph.nodes:
        visited[i] = False
    while( len(queue_1) != 0):
        n = queue_1.pop(0)
        if not visited[n]:
            queue_2.append(n)
        visited[n] = True
        m = graph.getFirst(n)
        while( m[1] != -1 ):
           # print(m[0])
           # print(visited[m[0]])
            if not visited[m[0]]:
                visited[n] = True
                queue_1.append(m[0])
            m = graph.getNext(n,m[1])
    return queue_2



if __name__ == "__main__":
    start_i, row, juzheng = fuck()
    graph = Graph(row, juzheng)
  #  graph.show()
   # print(BFS(graph,row[start_i]))
    for i in BFS(graph,row[start_i]):
        print(i,end=' ')
