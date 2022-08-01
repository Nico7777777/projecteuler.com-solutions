def ssq(n):
    answer = 0
    for i in range(n+1):
        answer += pow(i, 2)
    return answer


def sqs(m):
    answer = 0
    for j in range(m+1):
        answer += j
    return pow(answer, 2)


print (sqs(100) - ssq(100))
