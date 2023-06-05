class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        numMap = {}
        value = False
        for i in range(len(nums)):
            if nums[i] in numMap:
                value = True
                return value
            else:
                numMap[nums[i]] = i
        return value