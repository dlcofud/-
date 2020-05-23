def solution(s):
    key=[]
    s=s[2:-2]
    s=s.replace("{","[")
    s=s.replace("}","]")
    news=[]
    while len(s)>0:
        if s[0]=='[':
            s=s[1:]
            a=[]
            while s[0]!=']':
                if s[0]==']':
                    break
                a.append(int(s[0]))
                if s[1]==']':
                    s=s[1:]
                else:
                    s=s[2:]
        if s[0]==']':
            news.append(a)
            s=s[2:]
        if len(s)==0:
            break
            
            #문자열 튜플을 리스트로 변환
            
    news.sort(key=lambda x:len(x))
    
    #리스트를 크기순으로 정렬
    
    for x in range(len(news)):
        if len(key)==0:
            if len(news[0])>1:
                for i in range(len(news[0])):
                    key.append(int(news[0][i]))
            else:
                key.append(int(news[0]))
                
                #첫번째에 key리스트에 news의 첫번째 값 넣기
        else:
            for y in range(len(news[x])):
                if key.count(int(news[x][y]))==0:
                    key.append(int(news[x][y]))
                    break
                    
                    #news의 x번째 값이 key값에 없으면 
    return key
