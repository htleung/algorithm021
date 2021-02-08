#
# @lc app=leetcode.cn id=493 lang=python3
#
# [493] 翻转对
#

# @lc code=start
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(arr, left, right):
            if left>=right:
                return 0
            mid = (left+right)//2
            countleft = mergeSort(arr, left, mid)
            countright = mergeSort(arr, mid+1, right)
            countsep = merge(arr, left, mid, right)
            return countleft + countright + countsep
        def merge(arr, left, mid, right):
            temp = []
            i = left
            j = mid+1
            count = 0
            while i<=mid and j<=right:
                if arr[i]<=arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i<=mid:
                temp.append(arr[i])
                i+=1
            while j<=right:
                temp.append(arr[j])
                j+=1
            #计算逆序对
            ti = left
            tj = mid+1
            while ti<=mid and tj<=right:
                if arr[ti]<=2*arr[tj]:
                    ti+=1
                else:
                    count += mid-ti+1
                    tj+=1
            arr[left:right+1] = temp
            return count
        total = mergeSort(nums, 0, len(nums)-1)
        return total
# @lc code=end

