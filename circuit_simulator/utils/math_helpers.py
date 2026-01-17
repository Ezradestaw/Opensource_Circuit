import numpy as np

class MathHelpers:

    @staticmethod
    def rms(signal):
        """Root Mean Square of a signal"""
        return np.sqrt(np.mean(np.square(signal)))

    @staticmethod
    def db(value):
        """Convert linear value to decibels"""
        return 20 * np.log10(np.abs(value))

    @staticmethod
    def magnitude_phase(complex_number):
        """Return magnitude and phase (deg)"""
        mag = np.abs(complex_number)
        phase = np.angle(complex_number, deg=True)
        return mag, phase

    @staticmethod
    def safe_divide(a, b, default=0.0):
        """Avoid ZeroDivision errors"""
        return a / b if b != 0 else default

    @staticmethod
    def clamp(value, min_val, max_val):
        """Limit a value between min and max"""
        return max(min_val, min(value, max_val))
