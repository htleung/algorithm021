# 学习笔记
## 动态规划
1. 找出重复子问题  
2. 定义状态数组  
3. DP方程  

## 系列题目
### 爬楼梯(排列组合)
考虑顺序的是排列，不考虑顺序的是组合。本题记录一个在面试中遇到的将两者结合起来的问题。  
题目：n级台阶，一次允许走1级，2级。   
a) 一共有多少种走法   
b) 把a)的所有的走法都打印出来   
c) 如果不考虑先后顺序（比如3级台阶，先走1级再走2级和先走2级再走1级是 同一个解）一共有多少种走法  
d) 把c)都所有走法都打印出来  
题解：  
a)排列，相当于斐波拉契数，使用递推方程dp[i] = dp[i-1]+dp[i-2]  
b)要记录路径，可以将递推改成递归，并回溯，注意判断步数不要超过梯级数  
c)组合问题，动态规划，参考[零钱兑换II](https://leetcode-cn.com/problems/coin-change-2/submissions/)
```python
	def climb_permutation(n): 
		if n==1:
            return 1
        if n==2:
            return 2
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
```
```python
	def climb_permutation_print(n):
		def sub_climb(path, n):
			if sum(path)==n: #递归终止条件
				print(path)
			else:
				for step in [1,2]:
					path.append(i)
					if sum(path)<=n:#判断是否超过梯级数
						sub_climb(path, n)
					path.pop()#回溯
		path = []
		sub_climb(path, n)
```
```python
    def climb_combination(n):
		if n==0:
			return 1
		dp = [[0]*(n+1) for _ in range(2)]
		for j in range((n+1)):
			dp[0][j] = 1
		dp[1][0] = 1
		for j in range(1,(n+1)):
			if j>=2:
				dp[1][j] = dp[0][j] + dp[1][j-2]
			else:
				dp[1][j] = dp[0][j]
		return dp[-1][-1]
```
```python
	def climb_combination_print(n):
		def sub_climb(path, n, step):
			if sum(path)==n:
				print(path)
			else:
				for m in range(len(step)):
					for i in range(1,n//step[m]+1):
						for j in range(i):
							path.append(step[m])
						if sum(path)<=n:
							sub_climb(path, n, step[m+1:])
						for j in range(i):
							path.pop()
		path = []
		step = [1,2]
		sub_climb(path, n, step)
```
### 硬币兑换
### 打家劫舍
* [打家劫舍I](https://leetcode-cn.com/problems/house-robber/)  
	房间链式相连，递推方程dp[i]=max(dp[i-1](不偷第i个房间)，dp[i-2]+nums[i](偷第i个房间))
* [打家劫舍II](https://leetcode-cn.com/problems/house-robber-ii/)  
	房间环式相连，分为两种情况，偷第一个房间和不偷第一个房间
* [打家劫舍III](https://leetcode-cn.com/problems/house-robber-iii/)  
	房间树状相连，对树状结构进行动态规划，使用递归，对于每个节点，有偷和不偷两种情况，用哈希表记录每个节点的
	两种情况，对于一个节点，偷=节点的值+不偷左子节点+不偷右子节点，不偷=max(偷左子节点，不偷左子节点)+max(偷右子节点，不偷右子节点)
### 跳跃问题
### 股票买卖问题