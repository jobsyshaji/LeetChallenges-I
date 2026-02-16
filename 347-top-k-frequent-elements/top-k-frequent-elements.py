import collections
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if k == len(nums):
            return nums

        counts = collections.Counter(nums)
        
        return heapq.nlargest(k, counts.keys(), key=counts.get)