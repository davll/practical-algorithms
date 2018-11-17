# https://leetcode.com/problems/binary-subarrays-with-sum/

from collections import Counter

def num_subarrays_with_zero(A):
    ans, nz = 0, 0
    for x in A:
        if x == 0:
            nz += 1
        else:
            ans += ((nz+1)*nz) // 2
            nz = 0
    ans += ((nz+1)*nz) // 2
    return ans

def num_subarrays_v1(A, S):
    if S == 0:
        return num_subarrays_with_zero(A)
    else:
        indices = [i for i, x in enumerate(A) if x == 1]
        if not indices:
            return 0
        i, j = 0, S-1
        result = 0
        while j < len(indices):
            if i > 0:
                prefix = indices[i] - indices[i-1]
            else:
                prefix = indices[i] + 1
            if j < len(indices)-1:
                suffix = indices[j+1] - indices[j]
            else:
                suffix = len(A) - indices[j]
            #print("prefix[i={i}] = {p}".format(i=i, p=prefix))
            #print("suffix[j={i}] = {p}".format(i=j, p=suffix))
            result += prefix * suffix
            i, j = i+1, j+1
        return result

# Idea: Prefix Sum
#
# Find (i, j) so that P[j] - P[i] == S where i < j
# 
# for each j, count the number of i with P[j] = P[i] + S 
#
def num_subarrays_v2(A, S):
    P = [0] + A[:]
    for i in range(1, len(A)+1):
        P[i] += P[i-1]
    count = Counter()
    ans = 0
    for x in P:
        ans += count[x]
        count[x+S] += 1
    return ans

# Idea: Three Pointers
#
# for each j, count the number of i so that sum(A[i] ..A[j]) == S
#
# l = the smallest i so that sum_l <= S
# r = the hightest i so that sum_h <= S
# sum_l = sum(A[l] .. A[j])
# sum_r = sum(A[r] .. A[j])
#
# the number of subarray ending at j => (i_r - i_l + 1)
#
def num_subarrays_v3(A, S):
    #if S == 0:
    #    return num_subarrays_with_zero(A)
    result = 0
    l, r = 0, 0
    sum_l, sum_r = 0, 0
    for j, x in enumerate(A):
        # update sum_l
        sum_l += x
        # advance l when sum_l is too big
        while l < j and sum_l > S:
            sum_l -= A[l]
            l += 1
        # update sum_r
        sum_r += x
        # advance r when sum_r is too big or A[r] is not 1
        while r < j and (sum_r > S or A[r] == 0):
            sum_r -= A[r]
            r += 1
        #
        if sum_l == S:
            result += r - l + 1
    return result

class Solution:
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        return num_subarrays_v3(A, S)

#if __name__ == "__main__":
#    print(str(num_subarrays_v1([0, 0, 1, 0, 1, 0], 1)))
