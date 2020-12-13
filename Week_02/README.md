# 学习笔记
## 哈希表，映射，集合
* 哈希表: 通过把关键码值映射到表中的一个位置来访问记录，加快访问速度，用于映射的函数叫哈希函数， 常用的从哈希表抽象出来的两个结构：map, set
* map: python中的dict，key-value对
* set: python中的set，不重复的元素集合
## 树，二叉树，二叉搜索树
* 二维数据结构：树和图，树是无环的图
* 二叉树的遍历：前序，中序，后序, 层序遍历。前中后序可以用递归和迭代两种方法进行遍历，迭代主要通过栈来实现。层序通过队列来实现。
	* 前序
		* 递归
		```python
		def preorder(self,root)：
			if root:
				self.path.append(root.val)
				self.preorder(root.left)
				self.preorder(root.right)
		```
		* 迭代
		```python
		def preorder(self, root):
			if root is None:
				return []
			t = type(root)
			out = []
			stack = [root]
			while stack:
				root = stack.pop()
				if type(root)!=t and root is not None: #栈中既有node也有value，如果是value的话，则加入到结果数组中
					out.append(root)
					continue
				if root:
					stack.append(root.right) #子节点是将要访问的，所以压入栈中的是节点
					stack.append(root.left)
					stack.append(root.val)  #根节点已经访问过，所以压入栈中是它的value，出栈是直接将它的value加入结果即可
			return out
		```
	* 中序
		* 递归
		```python
		def inorder(self, root):
			if root:
				self.inorder(root.left)
				self.path.append(root.val)
				self.inorder(root.right)
		```
		* 迭代
		```python
		def inorder(self, root):
			if root is None:
				return []
			t = type(root)
			out = []
			stack = [root]
			while stack:
				root = stack.pop()
				if type(root)!=t and root is not None: 
					out.append(root)
					continue
				if root:
					stack.append(root.right) 
					stack.append(root.val)
					stack.append(root.left)  
			return out
		```
	* 后序
		* 递归
		```python
		def postorder(self, root):
			if root:
				self.postorder(root.left)
				self.postorder(root.right)
				self.path.append(root.val)
		```
		* 迭代
		```python
		def postorder(self, root):
			if root is None:
				return []
			t = type(root)
			out = []
			stack = [root]
			while stack:
				root = stack.pop()
				if type(root)!=t and root is not None: 
					out.append(root)
					continue
				if root:
					stack.append(root.val)
					stack.append(root.right) 
					stack.append(root.left)  
			return out
		```
	* 层序
	```python
	def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        out = []
        queue = [root]
        while queue:
            q_len = len(queue)
            level = []
            for i in range(q_len):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            out.append(level)
        return out
	```
* 二叉搜索树： 左子树的所有节点的值都小于根节点的值；右子树所有节点的值都大于根节点的值；左右子树都是二叉搜索树（重复性，因此树相关题目常用递归解决）；中序遍历后得到升序数组；
## 堆，二叉堆和图
### 堆
可以迅速从一堆数中找到最大或者最小值的数据结构；根为最大值则称为大根堆，根为最小值则称为小根堆
### 二叉堆
* 堆（优先队列）：完全二叉树
* 堆中节点的下标：节点i的左子节点是2*i+1，右子节点是2*i+2; 节点i的父节点是(i-1)//2;
* 堆常见操作的时间复杂度
	* find-max(min):O(1)
	* delete: O(logN)
	* insert: O(logN) or O(1)
* 常见操作简述
	* 插入：插入到堆的尾部，将节点与其父节点比较，逐层上浮
	* 删除堆顶元素：将堆顶元素与堆的最后一个节点交换，删除最后一个节点，将新的堆顶与其子节点比较，逐层下沉
* 常用于查找topk元素的题目
	* 查找topk大：小根堆，维持一个大小为k的小根堆，当有新元素时，将其与堆顶元素比较，若比堆顶大，则替换掉堆顶元素, 并heapifyDown
	* 查找topk小：大根堆，维持一个大小为k的大根堆，当有新元素时，将其与堆顶元素比较，若比堆顶小，则替换掉堆顶元素，并heapifyDown
### 图
* BFS：通过队列实现
* DFS：通过栈实现
* 注意：与树的遍历不同，图有可能有环，需要额外的visited数组来记录访问过的节点