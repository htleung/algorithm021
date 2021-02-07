# 学习笔记
## Trie树  
用于统计和排序大量字符串，经常被搜索引擎系统用于文本词频统计。  
优点：最大限度减少无效字符比较，查找效率比哈希表高。
基本性质：  
	* 节点本身不存完整单词，只存一个字符  
	* 从根节点到某一个节点，经过路径上的字符连起来，就是该节点对应的字符串  
	* 每个节点的不同子节点代表不同的字符  
核心思想：  
	* 公共前缀
	* 相当于26叉树(只考虑26个字母的情况下)，空间换时间  
python实现Trie  
python语法点：字典setdefault, dict.setdefault(key, default), 如果dict中有key, 返回dict[key],否则dict[key]=default, 并返回default值  
```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = '#'


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
                node = node[ch]
            else:
                node = node[ch]
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_of_word in node


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True
```

例题：[单词搜索II](https://leetcode-cn.com/problems/word-search-ii/)  
	- 暴力搜索：遍历words，对于每个word遍历board每个格子，进行dfs，假设有N个words，board为m\*n，单词长度为k，则时间复杂度为O(N*m*n*4^k)。  
	- 使用Trie记录words：先遍历words中的所有单词，形成一个Trie，然后遍历board，对每个格子搜索是否在Trie的root中，进行dfs，时间复杂度为O(N+m*n*4^k)=O(m*n*4^k)。  

## 并查集
适用场景：组团，配对，扩散感染  
基本操作：  
		- **makeSet(s)**: 建立一个新的并查集，其中包含s个单元素集合  
		- **unionSet(x,y)**: 将x和y所在的集合合并，用于x和y所在集合不相交的情况，如果x和y所在的集合相交则不合并  
		- **find(x)**: 找到x所在集合的代表  
数据结构：根据要求将元素分成不同的集合，每个集合有一个集合代表，每个元素都有一个指针，
该指针指向其所在集合的集合代表或者其父节点(可以将每个集合看成一棵子树，根据加入顺序生成的树)。可以用p[0..n]作为指针记录每个元素所在的集合。对于元素x，如果它就是所在集合的代表，那么p[x]=x    
初始化：每个元素自成一个集合，即p[i]=i  
并查集模板：
- 模板一：list实现  
```python
def init(self, p):
	p = [i for i in range(len(n))]
def unionSet(self, p, x, y):
	p1 = self.parent(p, x)
	p2 = self.parent(p, y)
	p[p1] = p2
def parent(self, p, x):
	root = p[x]
	while root!=p[root]:
		root = p[root]
	while x!=p[x]: #路径压缩，找到x所在集合的代表后，对路径进行压缩，路径上的每个节点的指针都指向集合代表
		temp = x
		x = p[x]
		p[temp] = root
	return root		
```

- 模板二：dict实现  
```python
def init(self,p):
	p = {}
def unionSet(self, p, x, y):
	p1 = self.parent(p, x)
	p2 = self.parent(p, y)
	p[p1] = p2
def parent(self, p, x):
	root = p.setdefault(x, x)
	while root!=p[root]:
		root = p[root]
	while x!=p[x]:
		temp = x
		x = p[x]
		p[temp] = root
	return root
``` 

## 高级搜索  
### n皇后，数独问题模板  
```python
def solve():
	result = [] #记录所有可行的解
	validset = set() #用set来记录当前状态，用于检查冲突
	DFS(level,curr_state) #DFS，逐层(一层可以代表一行(n皇后)，一个格子(数独)等等)深度优先搜索，可选解的个数少的优先探索，可以让生成树更小
def DFS(level, curr_state):
	#递归终止条件
	if curr_state satisfy condition:
		print_result()
	#探索下一层的分支
	for branch in level:
		if not valid: #检查冲突，如果存在冲突，则放弃当前分支的搜索，继续搜索下一个分支(剪枝)
			continue
		#如果没有冲突，用当前分支的值更新状态，继续下一层的探索
		update_validset()
		update_curr_state()
		DFS(level+1, curr_state)
		#回溯，恢复状态
		reset_validset()
		reset_curr_state()
def print_result():
	pass
```

### 双向BFS  
经典例题：[单词接龙](https://leetcode-cn.com/problems/word-ladder/)  
双向BFS模板一（两个队列表示两个方向，同时进行BFS）：    
```python
def twowayBFS(nodes):
	f_queue = []
	b_queue = []
	f_queue.append(beginNode)
	b_queue.append(endNode)
	visited_f = [False]*len(nodes)
	visited_b = [False]*len(nodes)
	level_f = 0
	level_b = 0
	while f_queue and b_queue:
		size_f = len(f_queue)
		size_b = len(b_queue)
		level_f += 1
		for _ in range(size_f): #前向BFS
			node = f_queue.pop(0)
			for i, n in enumerate(nodes):
				if not visited_f[i]:
					if isChild(node, n):
						if n==endNode:
							return level_f + 1
						visited_f[i] = True
						f_queue.append(n)
						if visited_b[i]:
							return level_f + level_b + 1
		level_b += 1
		for _ in range(size_b): #后向BFS
			node = b_queue.pop(0)
			for i, n in enumerate(nodes):
				if not visited_b[i]:
					if isChild(node, n):
						visited_b[i] = True
						b_queue.append(n)
						if visited_f[i]:
							return level_f + level_b + 1
	return 0
```  
双向BFS模板二：  
```python
def twowayBFS(nodes):
	f_queue = []
	b_queue = []
	f_queue.append(beginNode)
	b_queue.append(endNode)
	nodesSet = set()
	level = 0
	while f_queue and b_queue:
		size_f = len(f_queue)
		level += 1
		for _ in range(size_f):
			node = f_queue.pop(0)
			for n in nodesSet:
				if isChild(node, n):
					if n in b_queue:
						return level + 1
					nodesSet.remove(n)
					f_queue.append(n)
		if len(b_queue)<len(f_queue):
			b_queue, f_queue = f_queue, b_queue
	return 0		
```

### A*搜索  
代码模板  
```python
def AstarSearch(graph, start, end):
	pq = collections.priority_queue()
	pq.append([start])
	visited.add(start)
	while pq:
		node = pq.pop()
		visited.add(node)
		process(node)
		nodes = generate_related_nodes(node)
		unvisited = [node for node in nodes if node not in visited]
		pq.push(unvisited)
```