from src.base.solution import Solution
from src.tests.part2.q210_test_course_schedule_ii import CourseScheduleIiTestCases

class CourseScheduleIi(Solution):
    def run_test(self, input):
        return self.findOrder(input[0], input[1])

    def gen_test_cases(self):
        return CourseScheduleIiTestCases()

    def verify_output(self, test_output, output):

        res = set([])
        for lst in output:
            res.add('-'.join([str(x) for x in lst]))

        return '-'.join([str(x) for x in test_output]) in res

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        from collections import deque
        lkp, q, res = dict(), deque(), []

        for i in xrange(numCourses):
            lkp[i] = GraphNode(i)

        for edge in prerequisites:
            lkp[edge[0]].parents += 1
            lkp[edge[1]].children.append(lkp[edge[0]])

        for key in lkp:
            # print((key, lkp[key].is_root, lkp[key].color))
            if not lkp[key].parents: q.append(lkp[key])

        while q:
            node = q.popleft()

            for child in node.children:
                child.parents -= 1
                if not child.parents:
                    q.append(child)

            res.append(node.val)

        # print(res)
        return res if len(res) == numCourses else []



class GraphNode:

    def __init__(self, val):
        self.val = val
        self.parents = 0
        self.children = []


if __name__ == '__main__':
    sol = CourseScheduleIi()
    sol.run_tests()