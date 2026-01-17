import numpy as np

def bode_response(R, L, C, freqs):
    mag, phase = [], []
    for f in freqs:
        w = 2*np.pi*f
        Z = R + 1j*w*L + 1/(1j*w*C)
        H = 1/Z
        mag.append(abs(H))
        phase.append(np.angle(H, deg=True))
    return mag, phase
