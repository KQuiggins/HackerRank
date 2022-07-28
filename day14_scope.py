class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

	# Add your code here
    def computeDifference(self):
        x = 101
        y = 0

        for i in self.__elements:
            if i < x:
                x = i
            if i > y:
                y = i

        self.maximumDifference = y - x

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)