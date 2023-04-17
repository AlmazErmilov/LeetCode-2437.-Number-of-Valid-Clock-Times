def validClockTimes(time):
    comb = 1
    h1, h2, m1, m2 = time[0], time[1], time[3], time[4]

    if m2 == '?': comb *= 10
    if m1 == '?': comb *= 6

    if h2 == '?':
        if h1 == '?': 
            return comb * 24              # ??:mm

        elif h1 < '2': comb *= 10         # 0?:mm or 1?:mm
        else: comb *= 4                   # 2?:mm
    
    if h1 == '?': # 0, 1, 2               # ?0:mm
        if h2 < '4': comb *= 3            # ?3:mm
        else: comb *= 2                   # ?5:mm

    return comb
