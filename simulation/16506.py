import sys
N = int(input())
for i in range(N):
    s=list(sys.stdin.readline().split())
    bit4 = ''
    if 'C' in s[0]:
        bit4 = '1'
    else:
        bit4 = '0'
    s[0]= s[0].replace('C','')
    code = {'ADD':'0000','SUB':'0001','MOV':'0010','AND':'0011','OR':'0100','NOT':'0101','MULT':'0110','LSFTL':'0111','LSFTR':'1000','ASFTR':'1001','RL':'1010','RR':'1011'}[s[0]]
    code += bit4 + '0' + format(int(s[1]),'b').zfill(3)
    if s[0] == 'MOV' or s[0] =='NOT':
        code +='000'
    else:
        code += format(int(s[2]),'b').zfill(3)
    if bit4 == '0':
        code += format(int(s[3]),'b').zfill(3)+'0'
    else:    
        code += format(int(s[3]),'b').zfill(4)
    print(code)