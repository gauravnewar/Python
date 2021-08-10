def Add(b1,b2):
    sum =[]

    a = b1[7]
    b = b2[7]

    s = a^b
    c = a&b
    sum.append(s)

    for i in range(6,-1,-1):
        s = b1[i]^b2[i]^c
        c = (b1[i]&b2[i])|((b1[i]^b2[i])&c)
        sum.append(s)
    if c!=0:
        sum="not 8-bit operation."
        
    return sum
