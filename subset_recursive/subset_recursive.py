class Solution:
    ans = []
    a = []
    n = 0

    def rec(self, arr, ind):
        if ind == self.n:
            self.ans.append(arr)
            return

        self.rec(arr.copy(), ind + 1)

        arr.append(self.a[ind])
        self.rec(arr.copy(), ind + 1)

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.a = nums
        self.n = len(nums)
        arr = []
        self.rec(arr, 0)

        return self.ans