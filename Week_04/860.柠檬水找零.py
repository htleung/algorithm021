#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 5:0, 10:5, 20:15(5*3 or 10+5)
        five = 0
        ten = 0
        for b in bills:
            if b==5:
                five += 1
            elif b==10:
                if five>0:
                    five -= 1
                    ten += 1
                else:
                    return False
            elif b==20:
                if five>=1 and ten>=1:
                    five -= 1
                    ten -= 1
                elif five>=3:
                    five -= 3
                else:
                    return False
        return True
        
# @lc code=end

