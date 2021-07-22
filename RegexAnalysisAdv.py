import re
# \w matches with alpha numeric character
# + matches with one or more occurance of the pattern to its left
# \w* will match with every word including the whitespaces as * looks for 0 or more occurance
# of the pattern to its left
# Whereas, \w+ will matches with every word neglecting white spaces

result = re.findall(r'\w+', 'Python is the best programming language out there')

# find the first word in the string
result1 = re.findall(r'^\w+', 'Python is the best programming language out there')

# find the last word in the string
result2 = re.findall(r'\w+$', 'Python is the best programming language out there')

# . matches any single character except new line \n
# \b is word boundry
result3 = re.findall(r'\b\w.','Python is the best')

# Domain type of each email id
result4 = re.findall(r'@\w+.\w+', 'avinash@gmail.com, achyut@google.com, avinash@microsoft.com')

# only the domain name
result5 = re.findall(r'@\w+.(\w+)', 'avinash@gmail.com, achyut@google.com, avinash@microsoft.com')

print (result)
print (result1)
print (result2)
print (result3)
print (result4)
print (result5)