'''
Iterator for skyscrapers
Write a Python iterator
Instantiated over a list of ints
Produced values: each new maximum
Tops seen looking from left to right
Run over a random list
Print all produced values
'''
from random import shuffle

class SkyscraperIterator:
    def __init__(self, values):
        self.values = values
        self.index = 0
        self.max_value = float('-inf')
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.values):
            current_value = self.values[self.index]
            if current_value > self.max_value:
                self.max_value = current_value
                self.index += 1
                return self.max_value
            else:
                self.index += 1
                return next(self)
        else:
            raise StopIteration

# Generate a random list of integers
values = list(range(1, 6))
shuffle(values)

# Print the original list
print("Original list of values:", values)

# Create an iterator over the list of values
iterator = SkyscraperIterator(values)

# Iterate over the iterator and print each new maximum value
print("Skyscraper tops seen from left to right:")
for top in iterator:
    print(top)
