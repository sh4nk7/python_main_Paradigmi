class Operation:
    pass

class Sum(Operation):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

'''
Calculator
Write a Sum class, with two fields for its operands
Write a Product class, with two fields for its operands
Write a Negate class, with a single field
Write a Python calculate function
Params: an instance of Sum or Product or Negate
Return the result of the operation, as a textual message
In all other cases, return a textual error message
Use patterns (and guards, if really needed)
Possibly, define a common superclass
Otherwise, annotate the parameter of calculate
with all supported types, separated by |
'''

class Product(Operation):
    def __init__(self, operand1, operand2):
        self.operand1 = operand1
        self.operand2 = operand2

class Negate(Operation):
    def __init__(self, operand):
        self.operand = operand

def calculate(operation: 'Sum | Product | Negate') -> str:
    if isinstance(operation, Sum):
        result = operation.operand1 + operation.operand2
        return f"The sum of {operation.operand1} and {operation.operand2} is {result}."
    elif isinstance(operation, Product):
        result = operation.operand1 * operation.operand2
        return f"The product of {operation.operand1} and {operation.operand2} is {result}."
    elif isinstance(operation, Negate):
        result = -operation.operand
        return f"The negation of {operation.operand} is {result}."
    else:
        return "Error: Unsupported operation."

# Example usage:
# Create instances of Sum, Product, and Negate
sum_operation = Sum(3, 5)
product_operation = Product(4, 6)
negate_operation = Negate(7)

# Calculate results
print(calculate(sum_operation))        # Output: The sum of 3 and 5 is 8.
print(calculate(product_operation))    # Output: The product of 4 and 6 is 24.
print(calculate(negate_operation))     # Output: The negation of 7 is -7.

# Unsupported operation
unsupported_operation = "Unsupported"
print(calculate(unsupported_operation))  # Output: Error: Unsupported operation.
