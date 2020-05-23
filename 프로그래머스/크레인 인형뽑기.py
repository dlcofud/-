def solution(board, moves):
    answer = 0
    dolls=[]
    for x in range(len(moves)):
        location=moves[x]-1
        for y in range(len(board)):
            if board[y][location]!=0:
                dolls.append(board[y][location])
                board[y][location]=0
                break
        if len(dolls)>1 and dolls[-1]==dolls[-2]:
            dolls.pop()
            dolls.pop()
            answer+=2
    return answer
