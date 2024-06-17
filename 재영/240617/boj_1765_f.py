# 1765. 닭싸움 팀 정하기 - 시간초과
n = int(input())
m = int(input())

enemy = [[] for _ in range(n + 1)]
friend = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    s, a, b = input().split()
    a = int(a)
    b = int(b)
    if s == "E":
        enemy[a].append(b)
        enemy[b].append(a)
    else:
        friend[a][b] = 1
        friend[b][a] = 1

# 원수의 원수는 친구
for enemy_list in enemy[1:]:
    if len(enemy_list) >= 2:
        for student1 in enemy_list:
            for student2 in enemy_list:
                if student1 != student2:
                    friend[student1][student2] = 1
                    friend[student2][student1] = 1

# 친구의 친구는 친구
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if friend[i][k] and friend[k][j] and i != j:
                friend[i][j] = 1

check = [False for _ in range(n + 1)]
cnt = 0
for i in range(1, n + 1):
    if check[i]:
        continue
    for j in range(1, n + 1):
        if friend[i][j] == 1:
            check[j] = True
    cnt += 1
    check[i] = True

print(cnt)