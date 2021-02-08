# 学习笔记
## 位运算
### 位运算符  
```python
#左移
a<<1
#右移
a>>1
#按位或
a | b
#按位与
a & b
#按位取反
~a
#按位异或
a ^ b
```

### 指定位置的位运算  
- x最右边的n位清零： x & (~0<<n)
- 获取x的第n位：(x>>n)&1
- 获取x的第n位的幂值：x&(1<<n)
- 将第n位置为1：x|(1<<n)
- 将第n位置为0：x&(~(1<<n))
- x最高位至第n位清零：x&((1<<n)-1)

### 实战中常用的位运算  
- 判断奇偶: (x&1)==1; (x&1)==0
- x>>1：除以2
- 清零最低位的1：x&(x-1)
- 得到最低位的1：x&(-x)
- 得到0: x&(~x)

## 布隆过滤器
python代码实现：  
```python
from bitarray import bitarray
import mmh3
class BloomFilter:
	def __init__(self, size, hash_num):
		self.size = size
		self.hash_num = hash_num #一个元素用几个bit记录
		self.bit_array = bitarray(size)
		self.bit_array.setall(0)
	def add(self,s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s,seed)%self.size
			self.bit_array[result] = 1
	def lookup(self,s):
		for seed in range(self.hash_num):
			result = mmh3.hash(s,seed)%self.size
			if self.bit_array[result] == 0:
				return "Nope"
		return "Probably"
bf = BloomFilter(500000,7)
bf.add("happy")
print(bf.lookup("happy"))
print(bf.lookup("sad"))
```

## LRU cache  
实现: hash table + double linkedlist(双向链表关键：可以根据需要进行LIFO或者FIFO)  
```python
class DLinkedNode(object):
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head
    
    def addToHead(self, node):
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    def removeTail(self):
        prev = self.tail.prev
        prev.prev.next = self.tail
        self.tail.prev = prev.prev
        return prev
```
使用OrderedDict实现  
```python
class LRUCache(object):
	def __init__(self, capacity):
		self.dic = collections.OrderedDict() #根据key加入顺序形成的dict
		self.remain = capacity
	def get(self, key):
		if key not in self.dic:
			return -1
		v = self.dic.pop(key) #pop是python中dict的pop,弹出字典中的key元素
		self.dic[key] = v #再次加入key元素，这样key就变成了dict中最新的节点
		return v
	def put(self,key,value):
		if key in self.dic:
			self.dic.pop(key)
		else:
			if self.remain > 0:
				self.remain -= 1
			else:
				self.dic.popitem(last=False) #根据FIFO原则弹出，若last=True则根据LIFO原则
		self.dic[key] = value
```

## 排序算法  
- 比较类排序：冒泡排序，快速排序，插入排序，希尔排序，选择排序，堆排序，归并排序  
- 非比较类排序：计数排序，桶排序，基数排序  
- 十大排序的时间复杂度和空间复杂度（$O(n^2)$的为初级排序）  
	* 插入排序：时间$O(n^2)$, 空间$O(1)$，稳定  
	* 希尔排序：时间$O(n^2)$, 空间$O(1)$，不稳定  
	* 选择排序：时间$O(n^2)$, 空间$O(1)$，不稳定  
	* 冒泡排序：时间$O(n^2)$, 空间$O(1)$，稳定  
	* **堆排序：时间$O(nlogn)$, 空间$O(1)$，不稳定**
	* **快速排序：时间$O(nlogn)$, 空间$O(nlogn)$，不稳定**  
	* **归并排序：时间$O(nlogn)$, 空间$O(n)$，稳定**  
	* 计数排序：时间$O(n+k)$, 空间$O(n+k)$，稳定  
	* 桶排序：时间$O(n+k)$, 空间$O(n+k)$，稳定  
	* 基数排序：时间$O(n+k)$, 空间$O(n+k)$，稳定  
### 选择排序  
每次找最小值，然后放到待排序数组的起始位置  
python代码实现
```python
def selectionSort(arr):
	for i in range(len(arr)):
		minIndex = i
		for j in range(i+1,len(arr)):
			if arr[j]<arr[minIndex]:
				minIndex = j
		if minIndex!=i:
			arr[minIndex],arr[i] = arr[i],arr[minIndex]
```

### 插入排序
对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入
python代码实现：
```python
def insertionSort(arr):
	for i in range(1,len(arr)):
		curr = arr[i]
		preIndex = i-1
		while preIndex>=0 and arr[preIndex]>curr:
			arr[preIndex+1] = arr[preIndex]
			preIndex -= 1
		arr[preIndex+1] = curr
```

### 冒泡排序
嵌套循环，每次查看相邻的元素如果逆序，则交换
python代码实现：
```python
def bubbleSort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-i-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
```


### 快速排序
每次找一个pivot，然后将比它小的放在它的左边，比它大的放在右边，这样就将数组分成了两部分，再递归对两部分进行排序  
python代码实现：
```python
def quickSort(arr, left, right):
	if left<right:
		partitionIndex = partition(arr, left, right)
		quickSort(arr, left, partitionIndex-1)
		quickSort(arr, partitionIndex+1, right)
def partition(arr, left, right):
	pivot = left
	index = pivot+1 #循环结束后[pivot+1, index-1]这个区间内的数都比pivot小
	for i in range(index, right+1):
		if arr[i]<arr[pivot]:
			arr[i], arr[index] = arr[index], arr[i]
			index += 1
	arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
	return index-1 #返回pivot适当的位置
quickSort(arr, 0, len(arr)-1)
```

### 归并排序
快排：先调配处左右子数组，再对左右子数组进行排序  
归并：先对左右子数组进行排序，再合并两个子数组  
python代码实现：
```python
def mergeSort(arr, left, right):
	if right>=left:
		return
	mid = (left+right)//2
	mergeSort(arr, left, mid) #这一步结束后，子数组[left, mid]是有序的
	mergeSort(arr, mid+1, right) #这一步结束后，子数组[mid+1, right]是有序的
	merge(arr, left, mid, right)
def merge(arr, left, mid, right):
	temp = []
	i = left #指向左边有序数组，起始元素为left
	j = mid + 1 #指向右边有序数组，起始元素为mid+1
	while i<=mid and j<=right:
		if arr[i]<=arr[j]:
			temp.append(arr[i])
			i+=1
		else:
			temp.append(arr[j])
			j+=1
	while i<=mid:
		temp.append(arr[i])
		i+=1
	while j<=right:
		temp.append(arr[j])
		j+=1
	arr[left:right+1] = temp
mergeSort(arr, 0, len(arr)-1)
```

### 堆排序 

python代码实现：
```python
def heapsort(arr):
	#建立小根堆，(len(arr)-2)//2：最后一个元素的父节点
	for i in range((len(arr)-2)//2, -1, -1):
		heapify(i, len(arr), arr)
	#建立完成后，堆顶元素最小，每次将堆顶元素与最后一个元素调换，然后再维持堆性质
	for j in range(len(arr)-1, 0, -1):
		arr[j], arr[0] = arr[0], arr[j]
		heapify(0, j, arr)
def heapify(parent_index, length, arr):
	temp = arr[parent_index]
	left_child_index = 2*parent_index + 1
	right_child_index = 2*parent_index + 2
	while left_child_index<length:
		if arr[right_child_index]<arr[left_child_index]:
			child_index = right_child_index
		else:
			child_index = left_child_index
		if temp<arr[child_index]:
			break
		arr[parent_index] = arr[child_index]
		parent_index = child_index
		left_child_index = 2*parent_index + 1
		right_child_index = 2*parent_index + 2
	arr[parent_index] = temp
```

 

