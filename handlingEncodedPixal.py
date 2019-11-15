def encoded_pixel(a):
    x1,y1,x2,y2 = a
    epa = []
    #print(x1,y2)
    h = y2-y1
    ep = (1400*x1)+y1
    maxa = (1400*(x2+1))
    while (ep<maxa):
        epa.append(ep)
        epa.append(h)
        ep = ep+1400
    return epa
abc = encoded_pixel(a)
