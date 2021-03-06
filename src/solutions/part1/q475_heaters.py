from src.base.solution import Solution
from src.tests.part1.q475_test_heaters import HeatersTestCases

"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.


"""


class Heaters(Solution):
    def print_output(self, output):
        super(Heaters, self).print_output(output)

    def run_test(self, input):
        return self.findRadius(input[0], input[1])

    def gen_test_cases(self):
        return HeatersTestCases()

    def verify_output(self, test_output, output):
        return test_output == output

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters = sorted(heaters) + [float('inf')]
        print(heaters)
        i = r = 0
        for x in houses:
            while x - heaters[i] >= heaters[i+1] - x:
                i+=1
            r = max(r, abs(heaters[i]-x))
        return r

"""

    Binary Search 
    
    
    def findRadius(self, houses, heaters):
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int

        ht = heaters + [-10**9, 2*10**9 + 1]
        ht = sorted(ht)
        htlen = len(ht)
        max_radius = 0

        print(ht)

        for h in houses:
            si = 0
            ei = htlen - 1

            while ei - si > 1:
                k = (ei + si) / 2
                if h < ht[k]:
                    ei = k
                else:
                    si = k
            max_radius = max(max_radius, min(abs(ht[ei]-h), abs(h-ht[si])))

        return max_radius
"""


if __name__ == '__main__':
    heaters = Heaters()
    heaters.run_tests()