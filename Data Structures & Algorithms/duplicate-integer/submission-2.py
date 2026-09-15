class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myset=set()
        for value in nums:
            if value in myset:
                return True
            else:
                myset.add(value)
        return False
        