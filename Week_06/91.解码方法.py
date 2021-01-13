#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=='0':
            return 0
        if len(s)==1: #当只有一个数时，只有一种解码方式
            return 1
        dp = [0]*len(s) #状态矩阵dp记录子串s[0:i+1]的解码方式数
        dp[0] = 1 #初始化第一个位置
        if len(s)>1: #填充位置1
            if s[1]=='0': #'0'只能和前面的'1'或者'2'一起解码，无法单独解码
                if s[:2] in ['10', '20']:
                    dp[1] = 1
                else:
                    return 0 #无法解码
            else:
                if int(s[:2])<=26: #当两位数小于等于26时，有两种方式，既可以合在一起解码，也可以分开单个数字解码
                    dp[1]=2
                else: #当两位数大于26时，只能分开解码，因此只有一种方式
                    dp[1]=1
        for i in range(2,len(s)): 
            if s[i]=='0': #若当前数字为'0'，只能和前面的'1'或者'2'一起解码，如果前面不是'1''2'，则整个字符串无法解码
                if s[i-1:i+1] in ['10','20']:
                    dp[i] = dp[i-2]
                else:
                    return 0
            else:
                if s[i-1] == '0': #检查前面一位是否为'0'，是的话不能与前面一位组合，只能单独解码
                    dp[i] = dp[i-1]
                else:
                    if int(s[i-1:i+1])<=26:
                        dp[i] = dp[i-1] + dp[i-2]
                    else:
                        dp[i] = dp[i-1]
        return dp[-1]
# @lc code=end

