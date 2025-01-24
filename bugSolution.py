The OverflowError in this case can be handled by adding checks before the potentially problematic operations.

def handle_overflow(x):
    if x == float('inf') or x == float('-inf'):
        return "Infinity detected"
    try:
        result = float('inf') + x
        return result
    except OverflowError:
        return "Overflow occurred"

print(handle_overflow(10))
print(handle_overflow(float('inf')))
#The solution adds input validation to prevent the error from happening.