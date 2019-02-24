r = open("input.txt", 'r')
w = open("output.txt", "w")

wf = False
for line in r:
    print("number is", line)

s = int(line)
i = 9
while i > 1:
    if s % i == 0:
        s = s // i
        print("!!!is =", i)
        w.write(str(i))
        wf = True
    i = i - 1
if wf is False:
    w.write(str(-1))
r.close()
w.close()
