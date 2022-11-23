class Solution(object):
    def removeDuplicates(self, nums):
      k=len(nums)
      nums.append(nums[0])
      for i in range (0,k-1):
        if nums[i]!=nums[i+1]:
         nums.append(nums[i+1])
      del nums[:k]
      return len(nums)
            
        