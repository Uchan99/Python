def solution(n):
    answer = 0
    while n > 0:
        a = n % 10
        n //= 10
        answer += a
    return answer