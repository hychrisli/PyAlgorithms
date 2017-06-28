import abc


class TestCase(object):

    def __init__(self, name,  *input, *output):
        self.input = input
        self.output = output
        self.name = name