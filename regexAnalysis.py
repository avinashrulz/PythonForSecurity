import re
result = re.match(r'AV', 'AV Analytics ESET AV')
result1 = re.search(r'Analytics', 'AV Analytics ESET AV')
result2 = re.findall(r'Father', 'Father, Analytics ESET Fathers')
result3 = re.split(r's', 'AV Analytics ESET AV', maxsplit=1)
print (result)
print (result.group(0))
print (result1)
print (result1.group(0))
print (result2)
print (result3)
