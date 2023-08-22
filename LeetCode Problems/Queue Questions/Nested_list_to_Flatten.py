class NestedIterator:
    def __init__(self, nestedList):
        self.flatten_list = []
        self.index = 0
        self.flatten(nestedList)

    def flatten(self, nestedList):
        for i in nestedList:
            if i.isInteger():  # Check if it's an integer
                self.flatten_list.append(i.getInteger())
            else:
                self.flatten(i.getList())  # Recurse on the nested list

    def next(self):
        if self.hasNext():
            val = self.flatten_list[self.index]
            self.index += 1
            return val

    def hasNext(self):
        return self.index < len(self.flatten_list)


# Example usage
nestedList = [1, [2,3,[4,[6]]]]
iterator = NestedIterator(nestedList)

nestedList = [1, [2,3,[4,[6]]], [2]]
iterator = NestedIterator(nestedList)


