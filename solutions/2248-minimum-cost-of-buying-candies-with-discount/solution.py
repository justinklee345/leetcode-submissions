class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        
        cost = sorted(cost)
        counter = len(cost) - 1
        total = 0
        free = 2
        while counter >= 0:
            if free == 0:
                free = 2
                counter -= 1
                continue
            free -= 1
            total += cost[counter]
            counter -= 1

        return total

        
