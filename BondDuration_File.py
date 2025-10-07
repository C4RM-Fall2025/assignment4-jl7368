
def getBondDuration(y, face, couponRate, m, ppy = 1):
    t = m * ppy
    cf = couponRate * face / ppy
    pv = [(1 + y)**(-i) for i in range(1, t + 1)]
    cf_list = [cf if i < t - 1 else cf + face for i in range(t)]
    pvcf = [cf_list[i] * pv[i] for i in range(t)]
    pvcf_sum = sum(pvcf)
    weighted_times = sum([i * pvcf[i-1] for i in range(1, t + 1)])

    duration = weighted_times / pvcf_sum / ppy


    return duration