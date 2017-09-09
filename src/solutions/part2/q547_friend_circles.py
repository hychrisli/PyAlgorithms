from src.base.solution import Solution
from src.tests.part2.q547_test_friend_circles import FriendCirclesTestCases


class FriendCircles (Solution):
    def gen_test_cases(self):
        return FriendCirclesTestCases()

    def run_test(self, input):
        return self.findCircleNum(input)

    def findCircleNum(self, M):

        n = len(M)
        visited, cnt = [False] * n, 0

        def dfs(node):
            if visited[node]: return

            visited[node] = True
            for j, val in enumerate(M[node]):
                if val and not visited[j]:
                    dfs(j)

        for i in xrange(n):
            if not visited[i]:
                # print(visited)
                dfs(i)
                cnt += 1

        return cnt


if __name__ == '__main__':
    sol = FriendCircles()
    sol.run_tests()