def solution(set_menu, order):
    answer = ""
    for s in set_menu:
        if s[0] == order[0] and s[1] == order[1] and s[2] == order[2] :
            answer = s[3]
    return answer

print(solution([["bulgogi", "cider", "french fries", "6900"], ["chicken", "cider", "cheese stick", "7500"], ["shrimp", "coke", "cheese stick", "8200"]], 
               ["chicken", "cider", "cheese stick"]))