class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        num_concat = 2

        for i in range(num_concat):
            for n in nums:
                ans.append(n)
        
        return ans