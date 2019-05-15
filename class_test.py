

class TestClass(object):

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def add(self, val):
        self.attr1 = self.attr1 + val
        return self.attr1


out = TestClass(10, 100)
print(out.attr1)
print(out.add(200))
