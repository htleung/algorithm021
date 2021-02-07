class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #dfs做法
        # def dfs(i):
        #     for j in range(n):
        #         if isConnected[i][j] == 1 and j not in visited:
        #             visited.append(j)
        #             dfs(j)
        # count = 0
        # n = len(isConnected)
        # visited = []
        # for i in range(n):
        #     if i not in visited:
        #         visited.append(i)
        #         dfs(i)
        #         count += 1
        # return count
        
        #并查集做法
        n = len(isConnected)
        p = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    self._union(p,i,j)
        return len(set([self._parent(p,i) for i in range(n)]))
    
    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2
    
    def _parent(self, p, i):
        root = i
        while root!=p[root]:
            root = p[root]
        while i!=p[i]:
            x = i
            i = p[i]
            p[x] = root
        return root