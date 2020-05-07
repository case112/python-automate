import re

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

print(phone_num_regex.findall('Reguasd fsdim 345-345-1243 fdg  34345 234-234-2234 23424324342342334'))
