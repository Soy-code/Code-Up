# num3

# 승패승패승패 ...
def solution(score, target) :
    answer = 0
    while score < target :
        score += 10
        answer += 1
        if score >= target :
            break
        score -= 7
        answer += 1
    return answer


print(solution(50, 65))