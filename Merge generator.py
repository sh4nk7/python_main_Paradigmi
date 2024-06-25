''''
Merge generator
Define a merge generator function in Python
Takes two sorted sequences
Produces a sorted sequence, with all the elems
''''


def merge_generator(sequences1, sequences2):    
    iter1, iter2 = iter(sequences1), iter(sequences2)  
    valore1, valore2 = next(iter1, None), next(iter2, None)
    
    while valore1 is not None or valore2 is not None:
        if valore1 is None:
            yield valore2
            valore2 = next(iter2, None)
        elif valore2 is None:
            yield valore1
            valore1 = next(iter1, None)
        elif valore1 <= valore2:
            yield valore1
            valore1 = next(iter1, None)
        else:
            yield valore2
            valore2 = next(iter2, None)