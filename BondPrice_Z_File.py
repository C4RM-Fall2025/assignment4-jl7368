def getBondPrice_Z(face, couponRate, times, yc):
    cf = [face*(1+couponRate) if i == len(yc)-1 else face*couponRate for i in range(len(yc))]
    price = 0
    for i in range(len(yc)):
        pv = (1+yc[i])**(-times[i])
        price += cf[i]*pv

    return price
print(getBondPrice_Z(2000000, 0.04, [1,1.5,3,4,7]
, [.010,.015,.020,.025,.030]
))