import re

string = '(Булгаков) Обучающая_5 вместе.txt'


m = re.match('\((.+)\) (\S+)_', string)
m2 = re.match('\(Булгаков\) Обучающая_5 вместе\.txt', string)

if m:
    print(m[1])
    print(m[2])
else:
    print(False)