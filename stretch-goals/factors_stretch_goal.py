def factors(number):
    # ==============
    # Your code here
    list = []
    for i in range(2, number):
        if number % i == 0:
            list.append(i)
    if len(list) == 0:
        return (f'"{number} is a prime number"')
    else:
        return list
       
    # ==============

print(factors(15)) # Should print [3, 5] to the console
print(factors(12)) # Should print [2, 3, 4, 6] to the console
print(factors(13)) # Should print “13 is a prime number”
