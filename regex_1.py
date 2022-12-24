import re
value = "This is a string"
output = re.search("^This.*strings$",value)
print(output)

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[!@$%^&*()_+=-])(?=.{8,})"

# .: The period (dot) matches any single character, except for a newline.

# *: The asterisk matches zero or more of the preceding character or group. For example, "a*" will match zero or more "a" characters.

# +: The plus sign matches one or more of the preceding character or group. For example, "a+" will match one or more "a" characters.

# ?: The question mark matches zero or one of the preceding character or group. For example, "a?" will match zero or one "a" characters.

# ^: The caret matches the start of a string. For example, "^A" will match any string that starts with an uppercase letter A.

# $: The dollar sign matches the end of a string. For example, "world$" will match any string that ends with the word "world".

# |: The vertical bar represents an "or" condition. For example, "cat|dog" will match any string that contains either "cat" or "dog".

# [...]: Square brackets define a character set. For example, "[0123456789]" will match any digit.

# [^...]: A caret inside square brackets negates the character set. For example, "[^0123456789]" will match any character that is not a digit.

# (...): Parentheses define a capturing group. For example, "(\d\d\d)-(\d\d\d-\d\d\d\d)" will match a phone number and capture the area code and local number as separate groups.

# \d, \w, \s: These are shorthand character classes that match a digit, word character, or white space character, respectively.

# \1, \2, \3, etc.: These are backreferences that refer to a previously captured group. For example, "^(.+?)\s+\1$" will match any string that consists of two identical words separated by one or more spaces.