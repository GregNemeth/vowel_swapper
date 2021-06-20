def vowel_swapper(string):
    # ==============
    # Your code here
	return ('"' + string.replace('a', '4') \
    .replace('A', '4') \
    .replace('e', '3') \
    .replace('E', '3') \
    .replace('i', '!') \
    .replace('I', '!') \
    .replace('o', 'ooo') \
    .replace('O', '000') \
    .replace('u', '|_|') \
    .replace('U', '|_|') + '"')
    # ==============

print(vowel_swapper("aA eE iI oO uU")) # Should print "44 33 !! ooo000 |_||_|" to the console
print(vowel_swapper("Hello World")) # Should print "H3llooo Wooorld" to the console 
print(vowel_swapper("Everything's Available")) # Should print "3v3ryth!ng's 4v4!l4bl3" to the console