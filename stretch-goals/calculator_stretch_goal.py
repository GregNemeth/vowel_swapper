def calculator(a, b, operator):
    # ==============
    # Your code here
    result = 0
    

    if operator == "+":
        result = (a + b)
    elif operator == "-":
        result = (a - b)
    elif operator == "*":
        result = (a * b)
    else :
        if operator == "/":
         result = int(a / b)
    return bin(result).lstrip('0b')
    # ==============

print(calculator(2, 4, "+")) # Should print 110 to the console
print(calculator(10, 3, "-")) # Should print 111 to the console
print(calculator(4, 7, "*")) # Should output 11100 to the console
print(calculator(100, 2, "/")) # Should print 110010 to the console
