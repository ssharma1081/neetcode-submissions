class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        zipped = [(p, s) for p, s in zip(position, speed)]
        zipped.sort(key = lambda a: -a[0])
        
        for position, speed in zipped:
            timeToTarget = (target - position) / speed
            if not stack or timeToTarget > stack[-1]:
                stack.append(timeToTarget)
        return len(stack)
        
