# Q4: DevilGame
T = int(input())
re = []
for _ in range(T):
    n_i = int(input())
    
    if n_i % 4 == 0:
        re.append("false")
    else:
        re.append("true")
for re_ in re:
    print(re_)