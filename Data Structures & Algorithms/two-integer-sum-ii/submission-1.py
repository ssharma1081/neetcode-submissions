class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1,1,3,4]
        head = 0
        n = len(numbers)
        tail = n - 1
        while head < tail:
            sum = numbers[head] + numbers[tail]
            if sum == target:
                return [head + 1, tail + 1]
            elif sum < target:
                while (head + 1) < n and numbers[head + 1] == numbers[head]:
                    head += 1
                head += 1
            elif sum > target:
                while (tail - 1) < n and numbers[tail - 1] == numbers[tail]:
                    tail -= 1
                tail -= 1
            