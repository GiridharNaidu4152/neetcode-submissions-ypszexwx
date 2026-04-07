from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = Counter(nums)
        lit = sorted(data.keys(), key=lambda x: data[x], reverse=True)
        return lit[:k]