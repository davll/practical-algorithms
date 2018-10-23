class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = n // 2
        #print(str(m))
        nums.sort()
        #print(str(nums))
        ans = None
        prev = nums[0]
        count = 1
        for x in nums[1:]:
            #print("prev = {p}, count = {n}".format(p=prev, n=count))
            if prev == x:
                count += 1
            else:
                if count > m:
                    ans = prev
                prev = x
                count = 1
        if count > m:
            ans = prev
        return ans
