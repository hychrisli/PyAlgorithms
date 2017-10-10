from src.base.solution import Solution
from src.tests.part2.q394_test_decode_str import DecodeStrTestCases


class DecodeStr(Solution):
    def run_test(self, input):
        return self.decodeString(input)

    def gen_test_cases(self):
        return DecodeStrTestCases()

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk, cstr = [], ""

        for ch in s:
            if ch.isdigit():
                if cstr.isalpha():
                    stk.append(cstr)
                    cstr = ""
                cstr += ch
            elif ch.isalpha():
                cstr += ch
            elif ch == "[":
                stk.append(cstr)
                cstr = ""
            elif ch == "]":

                while stk[-1].isalpha():
                    cstr = stk.pop() + cstr

                cstr *= int(stk.pop())

        stk.append(cstr)

        return ''.join(stk)




    def decodeString_v1(self, s):
        """
        :type s: str
        :rtype: str
        """
        stk, bcnt, num, slst, rlst = [], 0, 0, [], []
        pre = ""

        for ch in s:
            if ch.isdigit():
                if not pre.isdigit():
                    rnum = num if num else 1
                    cstr = ''.join(slst)
                    if bcnt:
                        stk.append((rnum, cstr))
                    else:
                        rlst.append(rnum * cstr)
                    num, slst = 0, []

                num = num * 10 + int(ch)

            elif ch.isalpha():
                slst.append(ch)

            elif ch == '[':
                bcnt += 1

            elif ch == ']':
                bcnt -= 1
                rnum = num if num else 1
                tstr = rnum * ''.join(slst)
                if stk:
                    (num, lstr) = stk.pop()
                    slst = [lstr, tstr]
                else:
                    rlst.append(tstr)
                    num, slst = 0, []



            pre = ch

            # print((ch, stk, rlst, num))

        if stk:
            tt = stk.pop()
            rlst.append(tt[0] * tt[1])

        rlst.append(''.join(slst))

        return ''.join(rlst)



if __name__ == '__main__':
    sol = DecodeStr()
    sol.run_tests()