# 20437. 문자열 게임 2

def get_possible_length_from_idx_list(idx_lst, k):
    ret = set()
    for i in range(len(idx_lst)):
        if (i + k) > len(idx_lst):
            break
        ret.add(idx_lst[i + k - 1] - idx_lst[i] + 1)
    return ret


T = int(input())

for _ in range(T):
    word = input()
    K = int(input())

    count_dict = {}
    for char in word:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    idx_dict = {}
    for char_idx, char in enumerate(word):
        if count_dict[char] >= K:
            if char in idx_dict:
                idx_dict[char].append(char_idx)
            else:
                idx_dict[char] = [char_idx]

    if len(idx_dict) == 0:
        print(-1)
    else:
        min_length = len(word)
        max_length = 0

        for char in idx_dict:
            possible_length_set = get_possible_length_from_idx_list(idx_dict[char], K)
            if possible_length_set:
                min_length = min(min_length, min(possible_length_set))
                max_length = max(max_length, max(possible_length_set))

        print(min_length, max_length)