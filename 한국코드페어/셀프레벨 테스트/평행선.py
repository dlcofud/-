all=int(input())
for _ in range(all):
	n=int(input())
	tan=[[]for x in range(n-1)]
	x_list=[i+1 for i in range(n)]
	y_list=list(map(int,input().split(" ")))
	grow=0
	for x in range(n-1):
		for y in range(n):
			if y>grow:
				g=(y_list[y]-y_list[x])/(x_list[y]-x_list[x])
				tan[x].append(g)
		grow+=1
	print(tan)
