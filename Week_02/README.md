# 学习笔记
## 哈希表，映射，集合
* 哈希表: 通过把关键码值映射到表中的一个位置来访问记录，加快访问速度，用于映射的函数叫哈希函数， 常用的从哈希表抽象出来的两个结构：map, set
* map: python中的dict，key-value对
* set: python中的set，不重复的元素集合
## 树，二叉树，二叉搜索树
* 二维数据结构：树和图，树是无环的图
* 二叉树的遍历：前序，中序，后序遍历，可以用递归和迭代两种方法进行遍历，迭代主要通过栈来完成
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
## 堆，二叉堆和图