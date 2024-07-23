def solution(k, m, l):
    l.sort()
    answer = 0
    p = 0
    cnt = 0
    for i in range(0, k):
        while l[i] - l[p] > m:
            cnt -= 1
            p += 1
        cnt += 1
        answer = max(answer, cnt)
    return answer

print(solution(5, 4, [2,3,5,7,11]))