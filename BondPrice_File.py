

def getBondPrice(y, face, couponRate, m, ppy=1):
    price = 0.0
    t = m*ppy
    interest = couponRate * face / ppy

    for i in range(1, t+1):
        cf = interest
        if i == t:
            cf += face
        price += cf / (1 + y/ppy)**i

    return price
