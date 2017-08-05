
def split_by_space(s):

    si, res = 0, []

    for ei in xrange(len(s)):
        if s[ei] == ' ':
            res.append(s[si:ei])
            si = ei + 1

    res.append(str[si:])

    return res

def count_words(input_str):

    counter = dict()
    si, res = 0, []
    for ei in xrange(1,len(input_str)):
        if input_str[ei-1] == ' ':
            if input_str[ei] != ' ': si = ei # start of a word
        elif input_str[ei] == ' ': # end of a word
            word = input_str[si:ei]
            counter[word] = counter.get(word, 0) + 1

    if input_str[-1] != ' ':
        word = input_str[si:]
        counter[word] = counter.get(word, 0) + 1

    return counter


def count_str(input_str, sub_str):
    cnt, si = 0, 0
    for ei in xrange(1, len(input_str)):
        if input_str[ei-1] == ' ':
            if input_str[ei] != ' ': si = ei
        elif input_str[ei] == ' ':
            word = input_str[si:ei]
            if word == sub_str:
                cnt += 1

    if  input_str[si:] == sub_str: cnt += 1
    return cnt



if __name__ == '__main__':
    # print split_by_space("This is test 1")
    # print split_by_space("  This is test 1  ")
    # print count_words("This is is is test 1")
    # print count_words("This is   is is test 1   ")
    print count_str("This is   is is test 3 is", "is")