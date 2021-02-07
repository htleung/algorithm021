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
- 十大排序的时间复杂度和空间复杂度  
	| 排序算法 | 空间 | 时间 |  
	| --- | --- |
	|||
	|||
	|||
	|||
	|||
	|||
	|||
	