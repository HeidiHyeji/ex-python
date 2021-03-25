def r(N,M): #팀의 개수 구하기
	if N <=0 or M <=0: return 0
	return M if N/2 >= M else int(N/2)
N,M,K = map(int,input().split())
t=[]
t.append(r(N,M-K))#남자에게서만 인턴을 뽑을경우
t.append(r(N-K,M))#여자에게서만 인턴을 뽑을경우
#섞어서 뽑을경우
if N % 2 == 0 and N > 1: #여자가 짝수일 경우 여자를 짝수로 뽑는다 
	i = 1
	while 2*i<K:
		t.append(r(N-2*i,M-(K-2*i)))
		i+=1
elif N%2 == 1 and N > 0: #여자가 홀수일 경우 여자를 홀수로 뽑는다
	i = 1
	while 2*i-1<K:
		t.append(r(N-(2*i-1),M-(K-(2*i-1))))
		i+=1	
print(max(t))
