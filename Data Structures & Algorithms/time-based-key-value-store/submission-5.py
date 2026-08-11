class TimeMap:

    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
            
        if key not in self.mp:
            return ""
        vals = self.mp[key]
        # if len(vals) == 1:
        #     if vals[0][1] < timestamp:
        #         return vals[0][0]
        #     else:
        #         return ""
        l = 0
        r = len(vals) - 1
        while l <= r:
            mid = l + (r - l) // 2
            t = vals[mid][1]
            if timestamp == t:
                return vals[mid][0]
            elif timestamp < t:
                r = mid - 1
            else:
                l = mid + 1
        c = l - 1 if l > 0 else 0
        print(c)
        return vals[c][0] if timestamp > vals[c][1] else ""
