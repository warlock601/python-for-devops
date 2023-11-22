import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


# group() method returns the pattern that matches the substring in regular expression
# "re" implies regular exp
