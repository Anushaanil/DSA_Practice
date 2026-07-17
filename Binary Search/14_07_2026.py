class TimeMap:
    # Bruteforce
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = [[timestamp, value]]
        else:
            self.timemap[key].append([timestamp, value])
        
        print('set here: ', self.timemap)

    # # Bruteforce get method
    # def get(self, key: str, timestamp: int) -> str:
    #     if key not in self.timemap:
    #         return ""
    #     else:
    #         ans = ""
    #         for val in self.timemap[key]:
    #             if val[0] == timestamp:
                    # print('get here input: ', key, timestamp) 
                    # print('output', val[1], "\n")
    #                 return val[1]
                
    #             elif val[0] < timestamp:
    #                 ans = val[1]

    #         print('get here input: ', key, timestamp) 
    #         print('output', ans, "\n")

    #         return ans
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        else:
            l = 0
            r = len(self.timemap[key]) - 1
            ans = ""

            while l <= r:
                m = (l+r)//2
                val = self.timemap[key][m]

                if val[0] == timestamp:
                    return val[1]
                elif val[0] < timestamp:
                    ans = val[1]
                    l = m + 1
                else:
                    r = m - 1
                    
            return ans
        
        
class TimeMap:
    # Bruteforce
    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.timemap:
        #     self.timemap[key] = [[timestamp, value]]
        # else:
        #     self.timemap[key].append([timestamp, value])
        self.timemap.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
            
        values = self.timemap[key]
        left, right = 0, len(values) - 1
        ans = ""

        while left <= right:
            mid = (left+right)//2
            mid_timestamp, mid_val = values[mid]

            if mid_timestamp == timestamp:
                return mid_val
            elif mid_timestamp < timestamp:
                ans = mid_val
                left = mid + 1
            else:
                right = mid - 1
                
        return ans
            


# timeMap = TimeMap()
# timeMap.set("alice", "happy", 1) # store the key "alice" and value "happy" along with timestamp = 1.
# timeMap.get("alice", 1)         # return "happy"
# timeMap.get("alice", 2)         # return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
# timeMap.set("alice", "sad", 3)  # store the key "alice" and value "sad" along with timestamp = 3. 
# timeMap.get("alice", 3)

timeMap = TimeMap()
timeMap.set("test", "one", 10)
timeMap.set("test", "two", 20)
timeMap.set("test", "three", 30)
timeMap.get("test", 15)
timeMap.get("test", 25)
timeMap.get("test", 35)