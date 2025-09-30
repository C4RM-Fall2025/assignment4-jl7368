

def getBondPrice_E(face, couponRate, yc):
    cf = [face*(1+couponRate) if i == len(yc)-1 else face*couponRate for i in range(len(yc))]
    price = 0
    for i in range(len(yc)):
        pv = (1+yc[i])**(-i-1)
        price += cf[i]*pv
    
    return price
