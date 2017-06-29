import abc


class TestCase(object):

    def __init__(self, name, input_tup, output_tup):
        self.input_tup = input_tup
        self.output_tup = output_tup
        self.name = name