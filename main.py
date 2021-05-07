import ctypes
import numpy as np
from numpy import ctypeslib
import matplotlib.pyplot as plt
import time
from sklearn.metrics import mean_squared_error

class CPP():
    def __init__(self, path):
        self.cpp = ctypes.CDLL(path)

        self.dft = self.cpp.dft
        self.dft.argtypes = [ctypeslib.ndpointer(ctypes.c_double), ctypeslib.ndpointer(ctypes.c_double), ctypes.c_int]
        
        self.fft = self.cpp.fft
        self.fft.argtypes = [ctypeslib.ndpointer(ctypes.c_double), ctypes.c_int]

    def get_dft(self, N: int):
        t = np.arange(0, N, 1)
        x = 1*np.cos(2 * np.pi / 1024 * 500 * t)
        y = 0*np.sin(2 * np.pi / 1024 * 3 * t)

        input = np.column_stack((x, y))
        output = np.column_stack((x, y))

        start = time.time() * 1000
        self.dft(input, output, N)
        end = time.time() * 1000

        return (output, end-start)

    def get_fft(self, N: int):
        t = np.arange(0, N, 1)
        x = 1*np.cos(2 * np.pi / 1024 * 500 * t)
        y = 0*np.sin(2 * np.pi / 1024 * 3 * t)

        input = np.column_stack((x, y))

        start = time.time() * 1000
        self.fft(input, N)
        end = time.time() * 1000

        return (input, end-start)

