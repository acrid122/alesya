with open("9_5.txt") as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        pov3 = [i for i in s if s.count(i) == 3]
        if len(pov3) == 3 and pov3[0] % 2 != 0 and  (sum(s) - sum(pov3)) % 2 == 0:
            count += 1
    print(count)

    
with open("9_6.txt") as f:
    count = 0
    for i in f:
        s = list(map(int, i.split()))
        max_index = s.index(max(s))
        min_index = s.index(min(s))
        ras = max(s) - min(s)
        sp = sorted(s)
        ras_1 = sp[2] - sp[1]
        if 0 < max_index < 3 and min_index in [1, 2] and ras_1 != 0 and ras % ras_1 == 0: #сначала проверяем то, что неравно нулю
            count += 1
    print(count)