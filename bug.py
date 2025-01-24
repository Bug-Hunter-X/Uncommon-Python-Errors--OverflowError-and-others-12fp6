def function_with_uncommon_error(x):
    try:
        result = 10 / x
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

print(function_with_uncommon_error(0))  # Output: Division by zero
print(function_with_uncommon_error(2))  # Output: 5.0
print(function_with_uncommon_error("hello"))  # Output: Invalid input type

#Uncommon error: FloatingPointError

def uncommon_error_function(x):
    try:
        result = float('inf') + x
        return result
    except OverflowError:
        return "Overflow occurred"

print(uncommon_error_function(10))
print(uncommon_error_function(float('inf'))) #this will produce an OverflowError which is uncommon