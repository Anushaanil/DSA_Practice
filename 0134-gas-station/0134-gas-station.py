class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        s_index, cur_tank, total_tank = 0, 0, 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            cur_tank += gain
            total_tank += gain

            if cur_tank < 0:
                s_index = i + 1
                cur_tank = 0

        return s_index if total_tank >= 0 else -1