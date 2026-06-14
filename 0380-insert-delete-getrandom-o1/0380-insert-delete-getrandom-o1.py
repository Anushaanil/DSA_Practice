import random
class RandomizedSet:

    def __init__(self):
        self.randomset = {}
        self.randomlist = []

    def insert(self, val: int) -> bool:
        if val in self.randomset:
            return False
        self.randomlist.append(val)
        self.randomset[val] = len(self.randomlist)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.randomset:
            index_val = self.randomset[val]
            last_val = self.randomlist[-1]

            self.randomlist[index_val] = last_val
            self.randomset[last_val] = index_val

            self.randomlist.pop()
            self.randomset.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.randomlist)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()