def vowel_swapper(string):
    # ==============
    # Your code here
    new_string = []
    counter = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for i in range(len(string)):
        if string[i] == 'a':
            if counter['a'] == 0:
                new_string.append('a')
                counter['a'] += 1
            elif counter['a'] == 1:
                new_string.append('4')
                counter['a'] += 1
            else:
                new_string.append('a')
                counter['a'] += 1
        elif string[i] == 'A':
            if counter['a'] != 1:
                new_string.append('A')
                counter['a'] += 1
            elif counter['a'] == 1:
                new_string.append('4')
                counter['a'] += 1
        elif string[i] == 'e':
            if counter['e'] == 0:
                new_string.append('e')
                counter['e'] += 1
            elif counter['e'] == 1:
                new_string.append('3')
                counter['e'] += 1 
            else:
                new_string.append('e')
                counter['e'] += 1
        elif string[i] == 'E':
            if counter['e'] != 1:
                new_string.append('E')
                counter['e'] += 1
            elif counter['e'] == 1:
                new_string.append('3')
                counter['e'] += 1
        elif string[i] == 'i':
            if counter['i'] == 0:
                new_string.append('i')
                counter['i'] += 1
            elif counter['i'] == 1:
                new_string.append('!')
                counter['i'] += 1
            else:
                new_string.append('i')
                counter['i'] += 1
        elif string[i] == 'I':
            if counter['i'] != 1:
                new_string.append('I')
                counter['i'] += 1
            elif counter['i'] == 1:
                new_string.append('!')
                counter['i'] += 1
        elif string[i] == 'o':
            if counter['o'] == 0:
                new_string.append('o')
                counter['o'] += 1
            elif counter['o'] == 1:
                new_string.append('ooo')
                counter['o'] += 1
            else:
                new_string.append('o')
                counter['o'] += 1
        elif string[i] == 'O':
            if counter['o'] != 1:
                new_string.append('O')
                counter['o'] += 1
            elif counter['o'] == 1:
                new_string.append('000')
                counter['o'] += 1
        elif string[i] == 'u':
            if counter['u'] == 0:
                new_string.append('u')
                counter['u'] += 1
            elif counter['u'] == 1:
                new_string.append('|_|')
                counter['u'] += 1
            else:
                new_string.append('u')
                counter['u'] += 1
        elif string[i] == 'U':
            if counter['u'] != 1:
                new_string.append('U')
                counter['u'] += 1
            elif counter['u'] == 1:
                new_string.append('|_|')
                counter['u'] += 1         
        else:
            new_string.append(string[i])  
    
    return ('"' + ''.join(new_string) + '"')
    # ==============

print(vowel_swapper("aAa eEe iIi oOo uUu")) # Should print "a4a e3e i!i o000o u|_|u" to the console
print(vowel_swapper("Hello World")) # Should print "Hello Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "Ev3rything's Av4!lable" to the console
