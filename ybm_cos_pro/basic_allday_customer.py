# -> 이건 없어도 되지 않나
#class Customer:
#    def get_price(self):
#        pass

class BasicCustomer():
    def __init__(self, age, use_hour):
        self.age = age
        self.use_hour = use_hour

    def get_price(self):
        if self.age >= 18:
            return self.use_hour * 4000
        else: 
            return self.use_hour * 3000

class AllDayCustomer():
    def __init__(self, age, use_hour):
        self.age = age
        self.use_hour = use_hour

    def get_price(self):
        if self.age >= 18:
            return 20000
        else:
            return 15000


def solution(basic, allday):
    answer = 0

    for i in range(len(basic)):
        bc = BasicCustomer(basic[i][0], basic[i][1])
        answer += bc.get_price()

    for i in range(len(allday)):
        ad = AllDayCustomer(allday[i][0], allday[i][1])
        answer += ad.get_price()

    return answer

print(solution([[20, 2]], [[17, 1]]))
print(solution([[22, 3]], [[14, 2]]))