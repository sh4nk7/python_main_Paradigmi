'''
Exercise – Before we start
Write a Pyhton funtion
Given a list of positive integer values...
How many times does the maximum change?
Like counting the skyscrapers' tops
… which can be seen, looking from left to right
from random import shuffle
values = list(range(1, 6))
shuffle(values)  # e.g., [3, 1, 4, 2, 5]
def count_tops(values: list[int]) -> int:
    # …
'''

from random import shuffle

def count_tops(values: list[int]) -> int:
    # Check if the list is empty
    if not values:
        return 0
    
    # Initialize variables to keep track of the maximum value and count of tops
    max_value = values[0]
    count = 1
    
    # Iterate through the list starting from the second element
    for value in values[1:]:
        # If the current value is greater than the current maximum
        if value > max_value:
            # Update the maximum value and increment the count of tops
            max_value = value
            count += 1
    
    # Return the count of tops
    return count

# Generate a list of values and shuffle it
values = list(range(1, 6))
shuffle(values)  # e.g., [3, 1, 4, 2, 5]

# Print the shuffled list of values
print("List of values:", values)

# Call the count_tops function and print the result
print("Number of times maximum changes:", count_tops(values))

