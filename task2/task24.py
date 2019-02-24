from collections import defaultdict

inputs = input().split()
group_A = defaultdict(list)
group_B = defaultdict(list)

n = inputs[0]
m = inputs[1]

for index_1 in range(1, int(n) + 1):
    value = input().strip()
    group_A[value].append(str(index_1))

for index_2 in range(1, int(m) + 1):
    value = input().strip()
    group_B[value].append(str(index_2))

collection = list(group_B.keys())
collection.sort()

for each in collection:
    if each in group_A:
        print(' '.join(group_A[each]))
    else:
        print(-1)
