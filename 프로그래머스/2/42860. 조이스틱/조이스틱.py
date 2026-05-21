def solution(name):
    answer = 0
    n = len(name)

    # 1. 세로 이동
    for char in name:
        answer += min(ord(char) - ord('A'),
                      ord('Z') - ord(char) + 1)

    # 2. 가로 이동
    move = n - 1

    for i in range(n):
        next_idx = i + 1

        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        move = min(move,
                   2 * i + n - next_idx,
                   i + 2 * (n - next_idx))

    answer += move

    return answer