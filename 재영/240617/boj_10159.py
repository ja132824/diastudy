# 10159. 저울
N = int(input())
M = int(input())

adjM = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 인접 행렬
for _ in range(M):
    a, b = map(int, input().split())
    adjM[a][b] = 1
# print(adjM)

# i -> j 경로 있는지 확인
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if adjM[i][k] and adjM[k][j]:
                adjM[i][j] = 1
# print(adjM)

# i -> j, j -> i 경로가 다 없으면 대소 관계 알 수 없음
for i in range(1, N + 1):
    cnt = -1
    for j in range(1, N + 1):
        if adjM[i][j] == 0 and adjM[j][i] == 0:
            cnt += 1
    print(cnt)
