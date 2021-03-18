n = int(input())
res,cnt = 0,0
cnt = n//50000; res = n%50000
cnt += res//10000; res = res%10000
cnt += res//5000; res = res%5000
cnt += res//1000; res = res%1000
cnt += res//500; res = res%500
cnt += res//100; res = res%100
cnt += res//50; res = res%50
cnt += res//10; res = res%10
print(cnt)