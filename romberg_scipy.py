import numpy as np
from scipy import integrate

function = input("Masukkan fungsi yang diinginkan:\nf(x) = ")
f = lambda x: eval(function)
a = float(input("Masukkan batas bawah: "))
b = float(input("Masukkan batas atas: "))

result = integrate.romberg(f, a, b, show=True)
