# 1765. 닭싸움 팀 정하기

# 팀 대표 찾기
def find(i):
    if rep[i] == i:
        return i

    rep[i] = find(rep[i])
    return rep[i]


# 팀 합치기
def union(x, y):
    rep_x = find(x)
    rep_y = find(y)

    # 번호가 더 작은 쪽을 대표로
    if rep_x <= rep_y:
        rep[rep_y] = rep_x
    else:
        rep[rep_x] = rep_y


n = int(input())
m = int(input())

rep = [i for i in range(n + 1)]
enemy = [[] for _ in range(n + 1)]

for _ in range(m):
    s, a, b = input().split()
    a = int(a)
    b = int(b)
    if s == "E":
        enemy[a].append(b)
        enemy[b].append(a)
    else:
        union(a, b)

for enemy_list in enemy[1:]:
    if len(enemy_list) >= 2:
        for i in range(len(enemy_list)):
            for k in range(i + 1, len(enemy_list)):
                union(enemy_list[i], enemy_list[k])

teams = set()
for i in range(1, n + 1):
    teams.add(find(i))

print(len(teams))