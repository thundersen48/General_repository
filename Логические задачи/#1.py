#169
#Input: nums = [3,2,3]
#Output: 3
# Вывести элемент, который встречается больше всего
nums = [3,2,3]
class Solution:
    def majorityElement(self, nums: list[int])-> int:
        cache = {}
        cache = defaultdict(int)

        for num in nums:
            if num not in cache:
                cache.get(num, 0 ) + 1
        res = nums[0]
        max_count = 0
        for num, count in cahce.items():
            if count > max_count:
                max_count = count
                res = num
        return res
