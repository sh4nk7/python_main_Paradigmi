from functools import reduce

def compute_statistics(lst):
    max_changes, rooftops = reduce(process, lst, (0, 0))
    return max_changes, rooftops

def process(acc, x):
    max_val, max_so_far = acc
    if not max_so_far or x > max_val:
        max_val = x
        max_so_far = True
        rooftops = 1 if not max_so_far else 0
    else:
        rooftops = 1 if max_val > x else 0
    return (max_val, max_so_far), acc[1] + rooftops

# Example usage
lst = [3, 1, 4, 5, 2, 6, 7]
max_changes, rooftops = compute_statistics(lst)

print("Number of times maximum changes:", max_changes)
print("Number of visible rooftops:", rooftops)
