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
### 零钱兑换
* [零钱兑换I](https://leetcode-cn.com/problems/coin-change/)  
	凑成指定金额所需的最少硬币数量，动态规划状态记录dp[i]为凑成金额i所需的最少硬币数量，
	递推方程dp[i] = min(dp[i-c]+1 for all c in coins)
* [零钱兑换II](https://leetcode-cn.com/problems/coin-change-2/)  
	凑成指定金额的方法数。组合问题，动态规划状态记录矩阵dp[i][j]使用硬币[0..i]凑成金额j的方法数。
	递推方程dp[i] = dp[i-1][j] + dp[i][j-coins[i]]
### 打家劫舍
* [打家劫舍I](https://leetcode-cn.com/problems/house-robber/)  
	房间链式相连，递推方程dp[i]=max(dp[i-1](不偷第i个房间)，dp[i-2]+nums[i](偷第i个房间))
* [打家劫舍II](https://leetcode-cn.com/problems/house-robber-ii/)  
	房间环式相连，分为两种情况，偷第一个房间和不偷第一个房间
* [打家劫舍III](https://leetcode-cn.com/problems/house-robber-iii/)  
	房间树状相连，对树状结构进行动态规划，使用递归，对于每个节点，有偷和不偷两种情况，用哈希表记录每个节点的
	两种情况，对于一个节点，偷=节点的值+不偷左子节点+不偷右子节点，不偷=max(偷左子节点，不偷左子节点)+max(偷右子节点，不偷右子节点)
### 跳跃游戏
* [跳跃游戏I](https://leetcode-cn.com/problems/jump-game/)  
	问能否从第一个位置跳到最后一个位置，动态规划，从后往前遍历，用lastPos记录目前可以到达终点的最远的点。  
* [跳跃游戏II](https://leetcode-cn.com/problems/jump-game-ii/)  
	问到达最后一个位置最少要跳多少步，贪心算法，计算跳一步，跳两步，。。。，跳k步所能覆盖范围，直到到达最后一个位置  
* [跳跃游戏III](https://leetcode.com/problems/jump-game-iii/)  
	在位置i处，只可以往前或者往后跳arr[i]个单位，起始位置start，问能否跳到元素值为0的地方，BFS，二叉树遍历，看能否从根节点处到达元素值为0的节点，
	注意记录是否访问过的visited数组预先开辟len(arr)个位置，访问过的位置为True，否则为False。如果visited是list，每次访问过就append，会超时。
### 股票买卖问题    
[参考链接](https://leetcode-cn.com/circle/article/qiAgHn/)  
股票问题力扣上共有六道题，题目条件不同在于完成交易的次数和允许在哪些天交易(持有的股票都必须先卖出才能再买入)。    
改写版：  
	动态规划状态记录：在第i天有两种情况，持有和不持有  
		**dp[i][0]: 在第i天不持有股票所获得的收益**  
		**dp[i][1]: 在第i天持有股票所获得的收益**  
	动态规划基本递推式，后面的递推都是这个的变式：  
		**dp[i][0] = max(dp[i-1][0](不操作，维持在第i-1天时不持有情况的状态不变)，在第i天买入股票的收益计算式)**  
		**dp[i][1] = max(dp[i-1][1](不操作，维持在第i-1天时持有情况的状态不变)，在第i天卖出股票的收益计算式)**    
- [买卖股票的最佳时期I](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/)  
	只允许完成一次交易。  
	根据上述递推式，写出在每种情况下的收益递推式：
	
	**dp[i][1]**：在第i天持有股票，有两种可能性   
		1. 在第i-1天已经持有股票，且第i天不做任何操作，维持第i-1天状态，这时的收益与第i-1天一样，dp[i-1][1]  
		2. 在第i-1天不持有股票，而在第i天进行买入操作，这时的收益为在第i-1天不持有股票的收益，减去买入股票价格，即dp[i-1][0]-price[i]，又因为题目条件值能进行一次交易，因此在买入一定没有进行过交易，收益必定为0，dp[i][1] = 0-price[i]  
		第i天持有股票情况下的最大值就是上述两种可能性中的较大者。  
		初始化第一天，因为第一天不存在前一天持有的情况，所以第一天持有股票只可能是买入操作：dp[0][1]=-price[0]  
	
	**dp[i][0]**：在第i天不持有股票，有两种可能性  
		1. 在第i-1天已经不持有股票，且第i天不做任何操作，维持第i-1天状态，这时收益与第i-1天一样，dp[i][0]=dp[i-1][0]  
		2. 在第i-1天持有股票，而在第i天进行卖出操作，这时的收益为在第i-1天持有股票的收益，加上卖出股票价格，即dp[i-1][1]+price[i]  
		第i天不持有股票情况下的最大值就是上述两种可能性中的较大者。  
		初始化第一天，因为第一天本来就不会持有股票，也不能卖出，因此：dp[0][0]=0  
	
	完整的递推式为  
	$$dp[i][1] = max(dp[i-1][1], 0-price[i])$$
	$$dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i])$$  
	
	方法二：因为只进行一次交易，可以遍历股票价格，用变量minprice记录当前遍历过的最小价格，用变量maxprofit记录最大收益，遍历数组并更新这两个变量。
	
- [买卖股票的最佳时期II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/)  
	可以完成不限次数的买卖。  
	分析与第一题类似，唯一不同地方在于此题可以多次买卖，因此dp[i][1]中买入操作时的计算式是dp[i-1][0]-price[i]  
	此题的递推式为  
	$$dp[i][1] = max(dp[i-1][1], dp[i-1][0]-price[i])$$  
	$$dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i])$$  
	记得初始化dp[0][1] = -price[0]  
	
- [买卖股票的最佳时期III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/)  
	可以完成两次交易。  
	比起前两道题，本题多了一种交易次数状态的限制（第一题交易次数为1，每次考虑买入状态时必定为0，第二题交易次数不限制，按照递推式一直计算即可）  
	因此这里的状态数组要多一个维度，记录已经完成的交易次数。  
		**dp[i][0][0]: 完成0次交易，在第i天不持有股票所获得的收益**  
		**dp[i][1][0]: 完成1次交易，在第i天不持有股票所获得的收益**  
		**dp[i][0][1]: 完成0次交易，在第i天持有股票所获得的收益**  
		**dp[i][1][1]: 完成1次交易，在第i天持有股票所获得的收益**  
	写递推式时也要考虑多一种状态，本题的递推式为：  
		$$dp[i][0][0] = max(dp[i-1][0][0], dp[i-1][0][1]+price[i])$$  
		(完成0次交易时，在第i天不持有股票所获得的收益。有两种可能，一是完全没有进行过操作，即维持原来i-1天完成0次交易时不持有股票的状态，二是进行过一次买入操作，还没卖出，即在第i-1天完成0次交易情况下持有股票，在第i天卖出)  
		$$dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][1][1]+price[i])$$  
		(完成1次交易时，在第i天不持有股票所获得的收益。有两种可能，一是已经完成过一次买入卖出，维持原来i-1天完成1次交易时不持有股票的状态，二是已经进行了第二次买入，还没第二次卖出，在i-1天完成了1次交易情况下持有股票，在第i天卖出)  
		$$dp[i][0][1] = max(dp[i-1][0][1], 0-price[i])$$  
		(完成0次交易时，在第i天持有股票所获得的收益。有两种可能，一是维持原来第i-1天完成0次交易时持有股票的状态，二是在第i-1天完成0次交易情况下不持有股票，在第i天卖出，因为完成0次交易，因此和第一题一样第i-1天不持有股票的收益一定为0，直接0-price[i])    
		$$dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0]-price[i])$$  
		(完成1次交易时，在第i天持有股票所获得的收益。有两种可能，一是维持原来第i-1天完成1次交易时持有股票的状态，二是在第i-1天完成1次交易情况下不持有股票，也即完成了1次买入卖出，要进行第2次买入，参考第一个式子定义，使用dp[i-1][0][0]来计算)  
	初始化dp[0][0,1][1] = -price[0]

- [买卖股票的最佳时期IV](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)  
	可以完成k次交易。即第三题的进阶版，这时候记录完成交易次数的维度长度为k，即：  
		**dp[i][k][0]：完成k次交易时，在第i天不持有股票所获得的收益**  
		**dp[i][k][1]：完成k次交易时，在第i天持有股票所获得的收益**  
	分析第i天完成第k次交易时的两种情况：  
		**dp[i][k][0]**：维持第i-1天不持有股票的状态或者在第i天卖出股票。如果是在第i天卖出股票，即已经进行了k次交易(买入卖出)和第k+1次买入，此时使用dp[i-1][k][1]来计算，得到的结果就是第k+1次卖出后的收益。  
		**dp[i][k][1]**：维持第i-1天持有股票的状态或者在第i天买入股票。如果是在第i天买入股票，即已经进行了k次交易(买入卖出), 此时要使用第k次卖出后的收益来计算，根据dp[i][k][0]的定义，应该使用dp[i-1][k-1][0]。  
	当k=0时，计算dp[i][0][1]需要特殊处理，也即进行第一次买入时，此前还没有任何交易，因此dp[i][0][1] = 0-price[i]  
	本题的递推式为  
		$$dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1]+price[i])$$
		$$dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0]-price[i]) if j>0$$  
		$$dp[i][0][1] = max(dp[i-1][0][1], 0-price[i])$$  
	初始化dp[0][k][1] = -price[0]  
	还要考虑当k很大时，数组大小为n*k*2，可能会导致内存溢出。而题目条件是一天只能进行一个操作，所以一天买入一天卖出，n天最多只能进行n/2次交易，所以当k>n/2时，即问题相当于题目二，不限制交易次数。  

- [最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)  
	不限制交易次数，但是每次卖出后要冷却一天才能买入。这时候在计算dp[i][1]时需要使用dp[i-2][0]来计算。  
	递推式为：  
		$$dp[i][1] = max(dp[i-1][1], dp[i-2][0]-price[i])$$  
		$$dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i])$$  
	初始化dp[0][1]=-price[0]

- [股票买卖的最佳时机含手续费](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)  
	不限制交易次数，但是每次交易需要支付手续费fee。这时候在更新每次卖出收益时，需要减去手续费。  
	递推式为：  
		$$dp[i][1] = max(dp[i-1][1], dp[i-1][0]-price[i])$$  
		$$dp[i][0] = max(dp[i-1][0], dp[i-1][1]+price[i]-fee)$$  
	初始化dp[0][1]=-price[0]
		
### 不同路径
