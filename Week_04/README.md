# 学习笔记
## 深度优先与广度优先搜索
### 深度优先模板
* 递归写法
```python
	visited = set()
	def dfs(node, visited):
		if node in visited:
			return
		visited.add(node)
		for next_node in node.children():
			if next_node not in visited:
				dfs(next_node, visited)
```
* 迭代写法：使用栈
```python
	def dfs(root):
		visited,stack = [], [root]
		while stack:
			node = stack.pop()
			if node in visited:
				continue
			visited.append(node)
			process(node)
			for next_node in node.children():
				stack.append(next_node)			
```
### 广度优先模板
```python
	def bfs(root):
		visited, queue = [], [root]
		while queue:
			node = queue.pop(0)
			if node in visited:
				continue
			visited.append(node)
			process(node)
			for next_node in node.children():
				queue.append(next_node)
```  
记录路径可用：递归回溯记录path；队列/栈中记录路径而非单个节点；
## 贪心算法
* 每一步都是当下最优
* 与动态规划不同：不能回退，而动态规划记录下每一个阶段的结果，可以回退
* 贪心算法可以解决的一些问题：图的最小生成树；霍夫曼编码
## 二分查找
* 适用于有序，有上下边界的数组，关键在于各种边界和条件
	* 通用框架：左闭右闭，相应循环条件为while left<=right，移动搜索区间mid+1/-1
* 二分查找的三个情景
	* 查找一个元素
	```python
	def binarysearch(nums):
		left = 0
		right =len(nums)-1
		while left<=right:
			mid = (left+right)//2
			if target < nums[mid]:
				right = mid - 1
			elif target > nums[mid]:
				left = mid + 1
			elif target == nums[mid]:
				return mid
		return -1
	```
	* 查找左边界: 如leetcode35，找到第一个大于等于target的下标
	```python
	def leftboundsearch(nums):
		left = 0
		right = len(nums)-1
		while left<=right:
			mid = (left+right)/2
			if target < nums[mid]:
				right = mid - 1
			elif target > nums[mid]:
				left = mid + 1
			elif target == nums[mid]:
				right = mid - 1 //收紧右边界
		return left
	```
	* 查找右边界
	```python
	def rightboundsearch(nums):
		left = 0
		right = len(nums)-1
		while left<=right:
			mid = (left+right)/2
			if target < nums[mid]:
				right = mid - 1
			elif target > nums[mid]:
				left = mid + 1
			elif target == nums[mid]:
				left = mid + 1 //收紧左边界
		return right
	```
* 作业：使用二分查找，寻找一个半有序数组 [4, 5, 6, 7, 0, 1, 2] 中间无序的地方  
理解：与寻找旋转排序数组中的最小值类似，使用查找左边界或者查找右边界的方法都可以
```python
	def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        left = 0
        right = len(nums)-1
        if nums[right]>nums[left]:
            return nums[0]
        while left <= right:
            mid = (left+right)//2
            if mid>0 and nums[mid]<nums[mid-1]:
                return nums[mid]
            if mid<len(nums)-1 and nums[mid] > nums[mid+1]:
                return nums[mid+1]
            if nums[mid]>=nums[0]:
                left = mid+1
            elif nums[mid]<nums[0]:
                right = mid-1
```