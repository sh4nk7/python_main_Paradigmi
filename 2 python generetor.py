'''
Generator for skyscrapers
Write a Python generator
Instantiated over a list of ints
Produced values: each new maximum
Tops seen looking from left to right
Run over a random list
Print all produced values
'''

from random import shuffle

def skyscraper_tops(values):
    if not values:
        return
    
    max_value = values[0]
    yield max_value
    
    for value in values[1:]:
        if value > max_value:
            max_value = value
            yield max_value

# Generate a random list of integers
values = list(range(1, 6))
shuffle(values)

# Print the original list
print("Original list of values:", values)

# Iterate over the generator and print each new maximum value
print("Skyscraper tops seen from left to right:")
for top in skyscraper_tops(values):
    print(top)
