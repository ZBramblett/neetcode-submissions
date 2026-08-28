class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        val_reps = 0
        for i in range(len(nums)):
            if nums[i] == val:
                val_reps += 1
            else:
                k += 1
        for i in range(val_reps):
            nums.remove(val)
        return k