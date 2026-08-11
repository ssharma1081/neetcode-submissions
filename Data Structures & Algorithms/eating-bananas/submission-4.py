class Solution:
    def computeH(self, piles, speed):
        h = 0
        for pile in piles:
            h += math.ceil(pile / speed)

        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # the max number of bananas every hour is the highest threshold
        # 1 banana/hour is the lowest threshold
        # speed = [1,2,3,4] 
        # 3 bananas / hr => 5 hrs
        # 2 bananas / hr => 6 hrs
        # 1 bananas / hr => 10 hrs

        l = 1
        r = max(piles)
        res = float('inf')

        while l <= r:
            mid = l + (r - l) // 2
            t = self.computeH(piles, mid)
            # print(t)
            if t <= h:
                res = min(res, mid)
            if t <= h:
                r = mid - 1
            elif t > h:
                l = mid + 1
            # else:
            #     r = mid - 1
            #     break
        return res
            