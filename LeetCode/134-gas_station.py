# https://leetcode.com/problems/gas-station/
# https://leetcode.com/problems/gas-station/discuss/42666/Simple-O(n)-Java-solution-with-comments
# https://leetcode.com/problems/gas-station/discuss/191463/topic
# https://leetcode.com/problems/gas-station/discuss/141046/Python-solution-O(n)-time-O(1)-extra-space-beat-97

def complete_circuit_v1(gas, cost):
    N = len(gas)
    #
    for s in range(N):
        tank = 0
        for i in range(N):
            delta = gas[(i+s)%N] - cost[(i+s)%N]
            tank += delta
            if tank < 0:
                break
        if tank >= 0:
            return s
    return -1

def complete_circuit_v2(gas, cost):
    N = len(gas)
    #
    total, tank, index = 0, 0, 0
    for i in range(N):
        delta = gas[i] - cost[i]
        tank += delta
        if tank < 0:
            # if tank < 0, the circuit should start from i+1 instead
            index = i + 1
            tank = 0
        total += delta
    #
    if total < 0:
        return -1
    else:
        return index

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        return complete_circuit_v1(gas, cost)
