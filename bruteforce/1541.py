s = input()
num = s.replace('+','-').split('-')
op = [x for x in s if x not in ['0','1','2','3','4','5','6','7','8','9']]
op.insert(0,'+')

#+나오는 뒤는 최소로, -나오는 뒤는 최대로 만들기
