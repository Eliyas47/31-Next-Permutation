class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Modify nums in-place to the next lexicographically greater permutation.
        If no next permutation exists, rearrange nums to the smallest possible order.
        """
        # 1) Find the first index i from the right such that nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2) If i >= 0, find index j to swap
        if i >= 0:
            j = len(nums) - 1
            # Find the rightmost number > nums[i]
            while nums[j] <= nums[i]:
                j -= 1
            # Swap pivot with this number
            nums[i], nums[j] = nums[j], nums[i]

        # 3) Reverse the suffix after position i to get the smallest permutation
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
