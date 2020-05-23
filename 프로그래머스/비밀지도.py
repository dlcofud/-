def solution(n, arr1, arr2):
    answer = []
    secret=[[' ' for _ in range(n)]for _ in range(n)]
    for z in range(2):
        for x in range(n):
            if z==0:
                number=arr1[x]
            if z==1:
                number=arr2[x]
            number=bin(number)
            number=number[2:]
            if len(number)<n:
                addnumber='0'*(n-len(number))
                number=addnumber+number
            for y in range(n):
                if number[y]=='1':
                    secret[x][y]='#'
    for x in range(n):
        answer.append(''.join(secret[x]))
    return answer
