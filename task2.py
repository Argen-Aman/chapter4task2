import re

str_ = input('Enter some words (don\'t forget to put spaces between them):\n')
pattern = r'\s+'
# pattern = r'\W+'
result = re.split(pattern, str_)
for i in result:
    print(len(i))
