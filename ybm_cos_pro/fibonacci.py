# 주인장 마음대로 피보나치 수열
def fib(first, second, n) :
    if n == 1:
        return second 
    if n == 0:
        return first
    return fib(first, second, n-1) + fib(first, second, n-2)

# 첫째 항 & 둘째 항 = 1인 기본 피보나치 수열
fibo = lambda n: 1 if n <=2 else fibo(n-1) + fibo(n-2)

# answer
print(fib(2, 3, 5))
print(fibo(10))