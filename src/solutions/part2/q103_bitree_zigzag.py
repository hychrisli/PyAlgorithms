from src.base.solution import Solution
from src.tests.part2.q103_test_bitree_zigzag import BitreeZigzagTestCases

class BitreeZigzag(Solution):
    def gen_test_cases(self):
        return BitreeZigzagTestCases()

    def run_test(self, input):
        return self.zigzagLevelOrder(input)


    def zigzagLevelOrder(self, root):
        from collections import deque

        if not root: return []

        q, isLeft, res =  deque([root]), True, []

        while q:

            lvlres = []
            lvlcnt = len(q)

            while lvlcnt:
                node = q.popleft()
                # print(node.val, lvlcnt)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                lvlres.append(node.val)
                lvlcnt -= 1

            if isLeft:
                res.append(lvlres)
            else:
                res.append(lvlres[::-1])

            isLeft = not isLeft

        return res

    def zigzagLevelOrder_v1(self, root):
        """
        double stack
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []

        lstk, rstk, res = [root], [], []

        while lstk or rstk:

            lres = []
            while lstk:
                node = lstk.pop()
                lres.append(node.val)
                if node.left: rstk.append(node.left)
                if node.right: rstk.append(node.right)
            if lres: res.append(lres)
            rres = []
            while rstk:
                node = rstk.pop()
                rres.append(node.val)
                if node.right: lstk.append(node.right)
                if node.left: lstk.append(node.left)
            if rres: res.append(rres)

        return res




if __name__ == '__main__':

    sol = BitreeZigzag()
    sol.run_tests()