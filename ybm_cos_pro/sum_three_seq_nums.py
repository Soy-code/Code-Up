def solution(arr):
    answer = 0
    for i in range(0, len(arr) - 2):
        answer = max(answer, arr[i] + arr[i + 1] + arr[i + 2])
    return answer

print(solution([1, 5, 2, 4, 8, 8, 3]))