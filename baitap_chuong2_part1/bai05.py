st = input()
first5 = st[:5]
last5 = st[-5:]
one_line = (st + " ") * 4
four_lines = (st + "\n") * 4
print(first5)
print(last5)
print(one_line.strip())
print(four_lines.rstrip())
