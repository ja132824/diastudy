# 14002. 가장 긴 증가하는 부분 수열 4

n = int(input())
a = list(map(int, input().split()))

table = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            table[i] = max(table[i], table[j] + 1)

max_length = max(table)
print(max_length)
ans = []
max_idx = table.index(max_length)

while max_idx >= 0:
    if table[max_idx] == max_length:
        ans.append(a[max_idx])
        max_length -= 1
    max_idx -= 1

ans.reverse()
print(*ans)
