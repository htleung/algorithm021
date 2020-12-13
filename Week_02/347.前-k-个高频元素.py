#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def heapifyUp():
            endIdx = len(minHeap)-1
            while endIdx>0 and minHeap[(endIdx-1)//2][1] > minHeap[endIdx][1]:
                minHeap[endIdx], minHeap[(endIdx-1)//2] = minHeap[(endIdx-1)//2], minHeap[endIdx]
                endIdx = (endIdx-1)//2
        def heapifyDown():
            endIdx = len(minHeap)-1
            startIdx = 0
            while startIdx * 2 + 1 <= endIdx:
                child = startIdx*2 + 1
                if child + 1<=endIdx and minHeap[child][1]>minHeap[child+1][1]:
                    child = child + 1
                if minHeap[child][1] < minHeap[startIdx][1]:
                    minHeap[child], minHeap[startIdx] = minHeap[startIdx], minHeap[child]
                    startIdx = child
                else:
                    break

        numsDict = {}
        for n in nums:
            numsDict[n] = numsDict.get(n,0) + 1
        numCnt = [[key, numsDict[key]] for key in numsDict]
        minHeap = []
        for i in range(k):
            minHeap.append(numCnt[i])
            heapifyUp()
        for i in range(k, len(numCnt)):
            if numCnt[i][1] > minHeap[0][1]:
                minHeap[0] = numCnt[i]
                heapifyDown()
        res = [ele[0] for ele in minHeap]
        return res
# @lc code=end

