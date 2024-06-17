# 1943. 동전 분배
T = 3
for _ in range(T):
    N = int(input())
    coin_pair_arr = [None for _ in range(N)]
    total = 0
    for i in range(N):
        coin_pair_arr[i] = list(map(int, input().split()))
        total += coin_pair_arr[i][0] * coin_pair_arr[i][1]

    # print(coin_pair_arr)

    if total % 2 == 1:
        print(0)
        continue

    half = total // 2
    dp = [0 for _ in range(half + 1)]  # dp[i] 갖고 있는 동전으로 i원을 만드는 것이 가능한지
    dp[0] = 1

    for coin, cnt in coin_pair_arr:
        for i in range(half, coin - 1, -1):
            if dp[i - coin]:        # (i - coin)원을 만드는 게 가능하고 현재 coin 원의 동전을 cnt개 갖고 있으면 i원 (i + coin)원, (i + 2*coin)원, ... (i + (cnt - 1)*coin)원도 만들 수 있음
                for j in range(cnt):
                    if i + coin * j <= half:
                        dp[i + coin * j] = 1

    print(dp[half])
