import re

phone_num_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # ? - zero or one time

print(phone_num_regex.search('My number is  fsdim 234-345-1243 f4'))

bat_regex = re.compile(r'Bat(wo)*man') # * - zero or more

print(bat_regex.search('Batman')) 

bat2_regex = re.compile(r'Bat(wo)+man') # + - one or more

print(bat2_regex.search('Batman')) 

ha_regex = re.compile(r'(Ha){3}') # something {x} times

print(ha_regex.search('HaHaHa')) 
