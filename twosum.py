class Solution:
    def twoSum(self, nums, target):
        neednum = {}
        for i in range(len(nums)):
            if (nums[i] in neednum):
                return [neednum[nums[i]],i]
            else:
                neednum[target - nums[i]] = i
