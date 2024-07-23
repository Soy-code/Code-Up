def solution(lyrics):
    return sum([l.isalpha() for l in list(lyrics)])


print(solution("I love you."))