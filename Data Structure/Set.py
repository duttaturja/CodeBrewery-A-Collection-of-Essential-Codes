class Set:
    def __init__(self):
        self.elements = set()

    def add(self, element):
        self.elements.add(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def size(self):
        return len(self.elements)

# Example Usage
my_set = Set()
my_set.add(10)
my_set.add(20)
print(my_set.contains(10))  # Output: True
my_set.remove(10)
print(my_set.contains(10))  # Output: False
