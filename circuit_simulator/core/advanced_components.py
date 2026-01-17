def diode_current(v, Is=1e-12, n=1.7, Vt=0.026):
    return Is * (pow(2.718, v/(n*Vt)) - 1)

def bjt_gain(ic, beta=100):
    return ic * beta
