LN = input()

if '0' in LN:
	if sum(map(int,LN)) % 3 == 0: #3의 배수판정법 모든 자리의 합이 3의 배수이다
		print(int("".join(sorted(LN,reverse=True))))
	else:
		print(-1)
else:
	print(-1)