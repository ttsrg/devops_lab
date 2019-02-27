import re

f = open("input.txt", 'r')
w = open("output.txt", "w")
i = 1

for line in f:
    print("length =", len(line))

    if len(line) > 100:
        print(" file is more than 100 symbols")
        break

    if i > 1:
        print(" more than 1 strings")
        break

    print("i= ", i)
    print("line=", line)
    i = i + 1
s = str(line)
print(s)

line = s
print(re.match(r'(?P<n1>-?\d+)(?P<oper>'
               r'[-/*+])(?P<n2>-?\d+)=(?P<n3>-?\d+)$', line))

m = re.match(r'(?P<n1>-?\d+)(?P<oper>[-/*+])'
             r'(?P<n2>-?\d+)=(?P<n3>-?\d+)$', line)

if m is None:
    print("ERROR")
    w.write("ERROR")
    w.close()
    f.close()
    exit(1)

print("m.group () = ", m.group())
for i in range(1, 5):
    print("m.group", i, "= ", m.group(i))

n1 = int(m.group(1))
do = m.group(2)
n2 = int(m.group(3))
res = int(m.group(4))

if (abs(n1) or abs(n2) or abs(res)) > 30000:
    print("abs number more than  30000")
    w.write("incorrect data")
    w.close()
    f.close()
    exit(1)

if '+' in do and n1 + n2 == res or '-' in do and n1 - n2 == res \
        or '*' in do and n1 * n2 == res or '/' in do and n1 / n2 == res:
    print("correct expression")
    w.write("YES")
    w.close()
    f.close()
    exit(0)
else:
    print("non correct expression")
    w.write("NO")
    w.close()
    f.close()
    exit(1)

print("ERROR")
w.write("ERROR")
w.close()
f.close()
exit(0)
