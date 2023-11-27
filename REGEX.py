import re

# Task 1
print(re.findall("[Rr][Bb]+[Rr]", f"{input()}"))

# Task 2
print(re.fullmatch("(\d{4}-?){3}\d{4}", f"{input()}"))


# Task 3
def check(string: str):
    return re.fullmatch("[^-_][A-Za-z_]+-?[A-Za-z_]*", string)


print(check("as-d"))

# Task 4
print(re.fullmatch("[\dA-Za-z]{2,10}", input()))
