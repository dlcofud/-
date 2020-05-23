def solution(cacheSize, cities):
    answer = 0
    cityname=[]
    if cacheSize==0:
        answer=(len(cities)*5)
    else:
        for x in range(len(cities)):
            city=cities[x]
            city=city.upper()
            if cityname.count(city)==1:
                cityname.remove(city)
                cityname.append(city)
                answer+=1
            else:
                if cacheSize<=len(cityname):
                    cityname.pop(0)
                cityname.append(city)
                answer+=5
    return answer
