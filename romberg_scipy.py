import math
import numpy as np
from scipy import integrate

function = input("Enter the desired function (use x variable):\nf(x) = ")
f = lambda x: eval(function)
a = float(input("Enter the lower limit: "))
b = float(input("Enter the upper limit: "))

result = integrate.romberg(f, a, b, show=True)
