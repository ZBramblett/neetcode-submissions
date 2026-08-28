class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        max_consecutive = 0
        for i in range(len(nums)):
            if counter > max_consecutive:
                max_consecutive = counter
            if nums[i] == 1:
                counter += 1
            else:
                counter = 0

        if counter > max_consecutive:
                max_consecutive = counter
                
        return max_consecutive
            
