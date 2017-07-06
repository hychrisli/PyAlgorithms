from src.base.solution import Solution
from src.tests.q207_test_course_schedule import CourseScheduleTestCases

"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take.
    To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1.
So it is impossible.

"""

class CourseSchedule(Solution):
    def verify_output(self, test_output, output):
        return test_output == output

    def print_output(self, output):
        super(CourseSchedule, self).print_output(output)

    def gen_test_cases(self):
        return CourseScheduleTestCases()

    def run_test(self, input):
        return self.canFinish(input[0], input[1])

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        WHITE = 0
        GRAY = 1
        BLACK = 2

        class Node:
            def __init__(self, val):
                self.val = val
                self.color = WHITE
                self.children = []

        stack = []
        graph = dict()

        for i in range(numCourses):
            graph[i] = Node(i)

        for pre in prerequisites:
            graph[pre[0]].children.append(pre[1])

        for node in graph.values():
            # print(type(node))
            if node.color == WHITE:
                stack.append(node)
            while stack:
                # print(len(stack))
                cur_node = stack[-1]
                if cur_node.color == GRAY:
                    cur_node.color = BLACK
                    stack.pop()
                else:
                    """print(cur_node.val)
                    for node in graph.values():
                        print((node.val, node.is_visited, node.children))"""
                    cur_node.color = GRAY
                    for child in cur_node.children:
                        if graph[child].color == WHITE:
                            stack.append(graph[child])
                        elif graph[child].color == GRAY:
                            return False

        return True


if __name__ == '__main__':
    sol = CourseSchedule()
    sol.run_tests()