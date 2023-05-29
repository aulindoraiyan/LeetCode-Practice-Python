//answer in python:

    class Solution(object):
        def twoSum(self, nums, target):
        prevMap = {} #value , index

            for i, n  in enumerate(nums):  #In Python, enumerate is a built-in function used to iterate over a sequence (such as a list, tuple, or string) while keeping track of the index of each item. It returns an iterator that provides both the index and the corresponding value of each element in the sequence.
                diff = target - n   #i is index and n is number

                if diff in prevMap:
                return [prevMap[diff], i]
        prevMap[n]=i

            return
