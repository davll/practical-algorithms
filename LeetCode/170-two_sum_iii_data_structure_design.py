from collections import Counter

class TwoSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = Counter()
    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.numbers[number] += 1
    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for i in self.numbers.keys():
            j = value - i
            if j == i and self.numbers[j] >= 2:
                return True
            elif j != i and self.numbers[j] >= 1:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
