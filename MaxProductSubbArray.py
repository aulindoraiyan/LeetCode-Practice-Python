class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = max(
            nums)  # ekhane result max value of the array nisi cus what if there is a single element in the array. or like 2 element ase. having "0" or the first element will give wrong result

        currMin, currMax = 1, 1  # currMin o consider kortesi cus akta negative number diye multiply kore max and min er value reverse hoya jabe

        for i in nums:
            if i == 0:
                currMin = 1
                currMax = 1
                continue
            temp = i * currMax  # ekhane temp value ta banaisi cus or else currMin e updated currMax value chole jabe
            currMax = max(i * currMax, i * currMin, i)
            currMin = min(temp, i * currMin, i)
            result = max(result, currMax, currMin)

        return result