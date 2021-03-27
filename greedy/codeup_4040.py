'''
n,m = map(int,input().split())#n:여름 성수기 총기간, m:방의개수
r = [list(input()) for i in range(n)]
s,t = map(int,input().split()) #s: 펜션 도착, t:펜션떠나는날
s=s-1;t=t-1;cnt=0;flag = False
p = [0 for i in range(m)]
np = [0 for i in range(m)]
for j in range(s,t):
    for i in range(m):
        if r[j][i] == 'O':
            np[i]=1
        else:
            if p[i]!= 0 and max(p)==p[i] and p.count(p[i]) == 1: 
                flag=True
            np[i]=0
    if sum(np) == 0:
        cnt=-1
        break
    if flag:
        p=np
        cnt+=1
    else:
        for k in range(m):
            if np[k] == 0:
                p[k] = 0
            else:
                p[k]=p[k]+np[k]
    flag=False

print(cnt)

'''

room = []
#입력 변수 값을 int 형식으로 받기
n, m = map(int, input().split(" "))

for i in range(n) : #{
    room.append(input())
#}

s, t = map(int, input().split(" "))


# check 하기 위한 zeros_list
zeros_list = [0]*m

# 처음 방에 들어가거나 옮긴 후 예약 가능한 방을 확인해 해당 인덱스를 1로 넘겨줌
def new_check(day_data): #{
    result = [0]*m

    for idx, ox in enumerate(day_data) : #{
        if ox == "O" :  result[idx] = 1
    #}

    if result == zeros_list : return -1

    return result # 예를 들어 XXOXO라면 [0,0,1,0,1]로 return 해준다.
#}

# 최소로 옮기는 횟수를 세주는 함수
def check_max_day(room) : #{
    # 옮기는 횟수, 처음 부분을 제외하기 위해 -1 부터 시작한다.
    move = -1
    
    # 예약 가능한 방을 check 하기 위해 방의 개수만큼 list를 만들어준다. 
    check_list = [0]*m

	# 날짜 만큼 돌면서 예약 가능한 방을 check 해준다.
    for day_data in room : #{
    	# check_list에 묵을 수 있는 전날의 정보가 있다면, 이어서 묵을 수 있는 방을 check 해준다.
        if check_list != zeros_list :
            for idx, r in enumerate(check_list) : #{
            	# 전날 방에서는 묵을 수 있지만 오늘 묵지 못하면 0으로 표시를 바꿔준다.
                if r == 1 and day_data[idx] == 'X' : check_list[idx] = 0     
            #}

		# 만약 check_list가 모두 0이라서 방을 옮겨야 한다면, 예약 가능한 방을 check 해준다.
        if check_list == zeros_list :
        	# 방을 옮기므로 move + 1
            move += 1
            check_list = new_check(day_data)

			# 만약 예약 가능한 방이 없다면 -1를 리턴해준다.
            if check_list == -1 : return -1

    #}    
    return move
#}

# 손님이 묵는 날짜 만큼 room 예약 정보를 indexing 해준다.
room = room[s-1:t-1]
print(check_max_day(room))











