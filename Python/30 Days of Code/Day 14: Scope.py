class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        sortedElem = sorted(self.__elements)
        self.maximumDifference = sortedElem[-1] - sortedElem[0]


_ = input()
a = [int(e) for e in input().split(' ')]
d = Difference(a)
d.computeDifference()
print(d.maximumDifference)
