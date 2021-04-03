import sys

puz = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]
#0이 상하좌우 이동하는 것으로 보고 BFS 를 한다
# 최종 정렬된 상태가 될때까지
# visited 대신 퍼즐의 상태로 방문여부를 표시한다
mx = [0,0,-1,+1]
my = [-1,+1,0,0]
visited = [[] for _ in range(10)]#vistied[0]:0번째칸이 빈칸이였을때 숫자의 순서.리스트로 계속 추가한다
